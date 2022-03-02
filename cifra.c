#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct informacao{

	char nome[20];
	char dieta[15];
	int tempVida;
	int nivInt;
	float altura;
	float peso;

}registro;

void strupr(char string[20]){
	int i=0;
	while(string[i] != '\0'){
		string[i] = toupper(string[i]);
		i++;
	}
}

void decifra(registro *dado, int numReg){

	char nome[20], dieta[15], chave[15], c;
	int i = 0, j, k, tamChave;
	printf("Insira a palavra-chave:");
	scanf("%s", chave);
	strupr(chave);

	printf("\n\n DECODIFICANDO\n\n\n");
	while(i<numReg){

		j=0;
		k=0;
		strcpy(nome, dado[i].nome);
		strcpy(dieta, dado[i].dieta);
		strupr(nome);
		strupr(dieta);
		tamChave = strlen(chave);
		while(nome[j] != '\0'){
			c = nome[j] - abs(chave[k] - 'A');
			if(c < 'A')
				c += ('Z' - 'A') + 1;
			nome[j] = c;
			j++;;
			k++;;
			if(k >= tamChave){
				k=0;
			}
		}
		j=0;
		while(dieta[j] != '\0'){
			c = dieta[j] - abs(chave[k] - 'A');
			if(c < 'A')
				c += ('Z' - 'A') + 1;
			dieta[j] = c;
			j++;;
			k++;;
			if(k == tamChave)
				k=0;
		}
		strcpy(dado[i].nome, nome);
		strcpy(dado[i].dieta, dieta);
		i++;
	}
	for(i=0; i<numReg; i++){
		printf("Nome: %s\nDieta: %s\nVida: %d\nInteligencia: %d\nAltura: %.2f\nPeso: %.2f\n\n", dado[i].nome, dado[i].dieta, dado[i].tempVida, dado[i].nivInt, dado[i].altura, dado[i].peso);
	}
}

int lerBin(char mensagem[20]){

	FILE* f = fopen(mensagem, "r");

	if(f == NULL){
		printf("erro na abertura do arquivo\n");
		return -1;
	}

	int numReg, i;
	fread(&numReg, sizeof(int), 1, f);
	if(numReg < 1 || numReg >= 10){
		printf("Numero de especies incorreta\n");
		fclose(f);
		return -1;
	}
	registro dado[numReg];
	i = 0;
	fread(&dado, sizeof(registro), numReg, f);
	fclose(f);
	printf("\nNumero de especies = %d\n\n", numReg);

	for(i=0; i<numReg; i++){
		printf("Nome: %s\nDieta: %s\nVida: %d\nInteligencia: %d\nAltura: %.2f\nPeso: %.2f\n\n", dado[i].nome, dado[i].dieta, dado[i].tempVida, dado[i].nivInt, dado[i].altura, dado[i].peso);
	}

	decifra(dado, numReg);
	return 0;
}

int main(){

	char arq[20];
	int retorno;

	printf("Insira o Nome do Arquivo (inclua a extensao): ");
	scanf("%s", arq);

	retorno = lerBin(arq);
	if(retorno == -1)
		printf("\nErro na execução do programa\n");

	return 0;
}