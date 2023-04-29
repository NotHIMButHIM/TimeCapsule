#include<stdio.h>

#include<conio.h>

#include<windows.h> 

#define TRUE 1

#include<dos.h>

int main()
{
	int h=0,m=0,s=0,ms=0, danda; 
	
	Beep(700,300);

	{printf("***********WELCOME TO REMINDER DOCK SYSTEM (ALZHEIMER'S Project) ************* \n");
	
	 char task[90];

     printf("Name of the Reminder: \n");
     
     Beep(700,300);
     
	 scanf("%s",task);
     	
				printf("Now enter time:\n");
				
				scanf("%d%d%d",&h,&m,&s);
				
				Beep(700,300);

				while(1)
				
				{
					printf(" \r%d:%d:%d",h,m,s);

					Sleep(1000);
					
					Beep(700,300);   

					if(s!=0)

					{
						s--;
					}
					

					if(s==0 && m!=0)
					

					{
						s=59;
						m--;
					}

					if(s==0 && m==0 && h!=0)
					

					{
						h--;
						m=59;
						s=59;
					}
					
					if(h==0 && m==0 && s==3)
					
					
						{
						 printf("\nDo you want to snooze?\n1)YES\n2)NO\n");
						 
						 scanf("%d",&danda);
						 
						 Beep(700,300);
						 
						 switch(danda)
						 
						 {
						  case 1:
						 	
							 printf("\n******Thanks for using Reminder Dock******");
						  
						  case 2:
						  	
							break;
							
						 }
						 
						}
						
						
					if(h==0 && m==0 && s==0)
					
						{
							printf("\n********ITS TIME*********\n\n******Thanks for using Reminder Dock******");
								
							Beep(700,300);
								
							exit(0);
								
						}
					
				}
				
	}
	
}
