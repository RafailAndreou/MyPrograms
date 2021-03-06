// SDL.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <SDL.h>

using namespace std;

	int main(int argc, char *argv[]){
	SDL_Init(SDL_INIT_EVERYTHING);

	SDL_Window * window = NULL;
	window = SDL_CreateWindow("Title", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 400, 200, SDL_WINDOW_RESIZABLE);

	if (window == NULL) {
		cout << "ERROR" << SDL_GetError() << endl;
	}

	SDL_Surface *screen = SDL_GetWindowSurface(window);

	Uint32 white = SDL_MapRGB(screen->format, 255, 255, 255);

	SDL_FillRect(screen, NULL, white);
	SDL_UpdateWindowSurface(window);

	const SDL_MessageBoxButtonData buttons[] = {
	{ /*.flags, .buttonid, .text */       0, 0, "no" }, 
	{ SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT, 1, "yes" },
	{ SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT, 2, "cancel" },
	};
	const SDL_MessageBoxData messageboxdata = {
		SDL_MESSAGEBOX_INFORMATION, /* .flags */
		NULL, /* .window */
		"example message box", /* .title */
		"select a button", /* .message */
		SDL_arraysize(buttons), /* .numbuttons */
		buttons
	};
	int buttonid;
	if (SDL_ShowMessageBox(&messageboxdata, &buttonid) < 0) {
		SDL_Log("error displaying message box");
		return 1;
	}
	if (buttonid == -1) {
		SDL_Log("no selection");
	} 
	else {
		SDL_Log("selection was %s", buttons[buttonid].text);
		
		if (buttons[buttonid].buttonid == 0) {
			SDL_DestroyWindow(window);
			SDL_Quit();
		
		}  
};
	SDL_Event event;
	bool running = true;

	while (running) {
		while (SDL_PollEvent(&event))
		{
			if (event.type == SDL_KEYDOWN) {
				cout << event.key.keysym.sym;
			
			}
			if (event.type == SDL_QUIT) {
				running = false;
				break;
			}
		}
	}

	SDL_DestroyWindow(window);
	SDL_Quit();
    return 0;
	
}