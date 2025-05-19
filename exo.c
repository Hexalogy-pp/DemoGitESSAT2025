#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // Code du fils
        printf("Je suis le fils, je vais exécuter 'ls -l'\n");
        execl("/bin/ls", "ls", "-l", NULL);
        perror("Erreur exec");  // Ne s'affiche que si exec échoue
    }
    else if (pid > 0) {
        // Code du père
        printf("Je suis le père, mon fils a le PID %d\n", pid);
    }
    else {
        perror("Erreur fork");
    }

    return 0;
}

    