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
	surface = SDL_GetWindowSurface(window);		if (window == nullptr) 	std::cout << "Couldn't initialize: " << SDL_GetError() << std::endl;
}
class Rect {
public:
	SDL_Renderer * rend = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED );
	int PosX = 40, PosY = 40, VelX = 0, VelY = 0;
	SDL_Rect rect;

public:
	void handlevent(SDL_Event & e) {
		if (e.type == SDL_KEYDOWN) {
			switch (e.key.keysym.sym) {
			case SDLK_RIGHT: VelX += 15; break;
			case SDLK_LEFT:VelX -= 15; break;
			case SDLK_UP: VelY -= 15; break;
			case SDLK_DOWN: VelY += 15; break;
			}
			std::cout << "Pos: " << rect.x << " Vel: " << VelX << std::endl;
			std::cout << SDL_GetError() << std::endl;

		}
	}
	void move() {
		PosX = VelX;
		PosY = VelY;
		rect.x = PosX;
		rect.y = PosY;
		rect.h = 20;
		rect.w = 20;
		SDL_SetRenderDrawColor(rend, 0, 0, 255, 255);
		SDL_RenderFillRect(rend, &rect);
		SDL_RenderPresent(rend);
	}
};

void Quit() {
		SDL_FreeSurface(surface);
		SDL_DestroyWindow(window);
		SDL_DestroyRenderer(rend);
		SDL_Quit();
}

int main(int argc, char *argv[]) {

	Init();
	Rect box;
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
		SDL_RenderClear(rend);
		SDL_RenderPresent(rend);
}
	Quit();
	return 0;
}
