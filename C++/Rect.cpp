#include "pch.h"
#include<iostream>
#include "SDL.h"
#include "SDL_image.h"


SDL_Window * window = nullptr;
SDL_Surface * surface = nullptr;
SDL_Renderer * rend = nullptr;
SDL_Texture * text = nullptr;

void Init() {
	window = SDL_CreateWindow("SDL", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 500, 300, SDL_WINDOW_RESIZABLE);
}
class Rect{
public:
	SDL_Renderer * rend = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED );
	int PosX, PosY;
	SDL_Rect rect;

	Rect(int x,int y) {
		PosX = x;
		PosY = y;
	}

public:
	void handlevent(SDL_Event & e) {
		if (e.type == SDL_KEYDOWN) {
			switch (e.key.keysym.sym) {
			case SDLK_RIGHT: PosX += 15; break;
			case SDLK_LEFT:PosX -= 15; break;
			case SDLK_UP: PosY -= 15; break;
			case SDLK_DOWN: PosY += 15; break;
			}
		}
	}
	void move() {
		rect.x = PosX;
		rect.y = PosY;
		rect.h = 20;
		rect.w = 20;
		SDL_SetRenderDrawColor(rend, 0, 255, 255, 255);
		SDL_RenderFillRect(rend, &rect);
		SDL_RenderPresent(rend);
		if (SDL_SetRenderDrawColor(rend, 0, 255, 0, 0) != 0 || SDL_RenderClear(rend) != 0) {
			std::cout << SDL_GetError();
		}
	}
};

void Quit() {
		SDL_DestroyWindow(window);
		SDL_DestroyRenderer(rend);
		SDL_Quit();
}

int main(int argc, char *argv[]) {

	Init();
	Rect box(80,0);
	SDL_Event  event;
	bool running = true;
	while (running == true) {
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = false;
			}
			box.handlevent(event);
		}
		box.move();
}
	std::cout << SDL_GetError();
	Quit();
	return 0;
}
