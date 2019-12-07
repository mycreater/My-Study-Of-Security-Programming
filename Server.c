#define BUFSIZE 1000

#include <sys/fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <strings.h>

char *StrToUpper( char * );

int main () {
    int sockfd;
    int new_sockfd;
    int writer_len;
    struct sockaddr_in reader_addr;
    struct sockaddr_in writer_addr;
    char buf[BUFSIZE];

    int buf_len;

    /* Create Socket */
    if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) < 0 ) {
        perror("ERR: socket");
        exit(1);
    }

    /* Settings : Port & Address */
    bzero(&reader_addr, sizeof(reader_addr));
    reader_addr.sin_family = PF_INET;
    reader_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    reader_addr.sin_port = htons(8000);

    /* Assigning The Socket To The Address */
    if(bind(sockfd, (struct sockadder * ) &reader_addr, sizeof(reader_addr)) < 0 ) {
        perror("ERR: bind");
        exit(1);
    }

    /* Waiting */
    if(listen(sockfd, 3) < 0){
        close(sockfd);
        perror("ERR: listen");
        exit(1);
    }

    /* Requesting */
    if((new_sockfd = accept(sockfd, (struct sockaddr * ) &writer_addr, &writer_len)) < 0 ) {
        perror("ERR accept");
        exit(1);
    }

    /* Connection */
    buf_len = read(new_sockfd, buf, BUFSIZE);
    write(1, buf, buf_len);
    write(new_sockfd, StrToUpper(buf), buf_len);

    /* Close Socket */
    close(new_sockfd);
    close(sockfd);
}

/* Character : Lower To Upper */
char *StrToUpper (char *s) {
    char *t;

    for( t = s; *t; t++ ){
        *t = toupper(*t);
    }
    return(s);
}