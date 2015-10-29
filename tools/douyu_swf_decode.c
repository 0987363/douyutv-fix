#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <errno.h>

const char *key = "dkrltl0%4*@jrky#@$";


int main(int argc, char **argv) {
    if (argc < 2) {
        printf("need swf file\n");
        exit(-1);
    }

    char *file = argv[1];

    struct stat statbuff;  
    if (stat(file, &statbuff) < 0) {  
        printf("get file size failed:%s\n", file);
        exit(-1);
    }  
    int file_size = statbuff.st_size;  
    int key_size = strlen(key);

    int fd = open(file, O_RDONLY);
    if (fd < 0) {
        printf("open file:%s failed, err:%s\n", file, strerror(errno));
        exit(-1);
    }

    char *new_file = (char *)calloc(1, 300);
    int len = strlen(file);
    while (len-- > 0) {
        if (file[len] == '.') 
            break;
    }
    switch (len) {
        case -1:
            sprintf(new_file, "%s_new.swf", file);
            break;
        case 0:
            printf("file failed:%s\n", file);
            exit(-1);
        default:
            memcpy(new_file, file, len);
            strcat(new_file + len, "_new.swf");
            break;
    }

    int new_fd = open(new_file, O_CREAT | O_TRUNC | O_RDWR);
    if (new_fd < 0) {
        printf("open file:%s failed, err:%s\n", new_file, strerror(errno));
        exit(-1);
    }

    int key_idx = 0;
    int idx2 = 0;
    int index = 0;
    char *buf = (char *)calloc(1, file_size);
    int n = 0;
    while (index < file_size) {
        if (key_idx >= key_size) {  //18
            key_idx = 0;
            idx2++;
            if (idx2 >= 50) {
                int remain = file_size - 50 * key_size;
                n = read(fd, buf, file_size - 50 * key_size);
                if (n != remain) {
                    printf("read remain:%d, real len:%d\n", remain, n);
                    exit(-1);
                }
                write(new_fd, buf, remain);
                break;
            }
        }
        n = read(fd, buf, 1);
        if (n <= 0) {
            printf("read file:%s failed\n", file);
            exit(-1);
        }
        buf[0] -= key[key_idx];
        write(new_fd, buf, 1);
        index++;
        key_idx++;
    }

    close(fd);
    close(new_fd);
    return 0;
}




