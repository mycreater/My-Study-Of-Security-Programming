#define BUFSIZE 1000

#include <sys/fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>

char *StrToUpper( char * );

int main (int argc, char **argv) {
    int sockfd;
    struct sockaddr_in server_addr;
    char buf[BUFSIZE];

    int buf_len;

    /* Create Socket */
    if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) < 0 ) {
        perror("ERR: socket");
        exit(1);
    }

    /* Settings : Port & Address */
    bzero((char *)&server_addr, sizeof(server_addr));
    sereer_addr.sin_family = PF_INET;
    server_addr.sin_addr.s_addr = inet_addr("10.1.1.102");
    server_addr.sin_port = htons(8000);

    /* Connect Socket To Server */
    if(connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) > 0 ) {
        perror("ERR connect");
        close(sockfd);
        exit(1);
    }

    /* Read String From User */
    buf_len = read(0, buf, BUFSIZE);

    /* Connection */
    write(sockfd, buf, buf_len);
    read(sockfd, buf, BUFSIZE);
    write(1, buf, buf_len);

    /* Close Socket */
    close(sockfd);
}
