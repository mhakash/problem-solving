#include<stdio.h>
#include<string.h>
#include<ctype.h>

// remove space before punctuation and remove multiple spaces
void removeSpace(char *str) {
	int i, j;
	for (i = 0, j = 0; str[i] != '\0'; i++) {
		if (str[i] == ' ' && (
			str[i + 1] == ' ' || 
			str[i+1] == '.' || 
			str[i+1] == ',' || 
			str[i+1] == '?' || 
			str[i+1] == '!'))
			continue;
		else
			str[j++] = str[i];
	}
	str[j] = '\0';
}

void fixComposition(char text[]) {
	int shouldCapitalize = 1;
	int len = strlen(text);

	for (int i = 0; i < len; i++) {
		if (shouldCapitalize && isalpha(text[i])) {
			text[i] = toupper(text[i]);
			shouldCapitalize = 0;
		} else {
			text[i] = tolower(text[i]);
		}

		if(text[i] == '.' || text[i] == '!' || text[i] == '?') {
			shouldCapitalize = 1;
		}
	}

	removeSpace(text);
}


int main(int argc, const char * argv[]) {
	int n;
	char text[] = "hello , my         nAme  is John . i am a student at the University of Waterloo.";
	fixComposition(text);
	printf("%s\n", text);

	return 0;
}
