#include <stdio.h>

int check_os(void)
{
    #ifdef _WIN32
        #ifdef _WIN64
            printf("\nYou are using 64 bit windows\n");
        #else
            printf("\nYou are using 32 bit  windows\n");
        #endif
    #endif
    #ifdef __unix__
        #ifdef __linux__
            #ifdef __android__
                printf("\nYou are using an android based device\n");
            #else
                printf("\nYou are using a linux based distro\n");
            #endif
        #else
            printf("\nYou are using unix based distro");
        #endif
    #endif
    #ifdef __APPLE__
        #ifdef TARGET_OS_MAC  
            printf("\nYou are using Mac OS\n");
        #endif
        #ifdef TARGET_OS_IPHONE
            printf("\nYou are using an iPhone\n");
        #endif
        #ifdef  TARGET_IPHONE_SIMULATOR
            printf("\nYou are running this on an iOS simulator\n");
        #endif
        #ifdef  TARGET_OS_EMBEDDED
            printf("\nYou are running this on an embeded device running iOS\n");
        #else
            printf("\nYou are using an Apple based OS\n"); 
        #endif
    #endif
    #ifdef BSD
        printf("\nYou are using a BSD based OS\n");
    #endif
    return 0;
}

int main()
{
    check_os();
}
