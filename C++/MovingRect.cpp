#include "pch.h"
#include<iostream>
#include "SDL.h"
#include "SDL_image.h"

SDL_Window * window = nullptr;
SDL_Surface * surface = nullptr;
SDL_Renderer * rend = nullptr;

void Init() {
	window = SDL_CreateWindow("SDL", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 500, 300, SDL_WINDOW_RESIZABLE);
		if (window == nullptr) 	std::cout << "Couldn't initialize: " << SDL_GetError() << std::endl;
}

class Rect {
public:
	int x, y;
	SDL_Surface * surface = SDL_GetWindowSurface(window);
	SDL_Rect rect;
	SDL_Renderer * rend = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
public:
	Rect(int x, int y, int w, int h) {
		this->x = x;
		this->y = x;
		rect.x = x;
		rect.y = y;
		rect.w = w;
		rect.h = h;
		SDL_SetRenderDrawColor(rend, 0, 0, 255, 255);
		SDL_RenderFillRect(rend, &rect);
		SDL_RenderPresent(rend);
		SDL_DestroyRenderer(rend);
		std::cout << SDL_GetError() << std::endl;
	}
};
void Quit() {
		SDL_FreeSurface(surface);
		SDL_DestroyWindow(window);
		SDL_DestroyRenderer(rend);
		SDL_Quit();
}

int main(int argc,char *argv[]) {

	Init();
	Rect box(200, 100, 100, 100);
	SDL_Event  event;
	bool running = true;
	while (running == true) {
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = false;
			}
			else if (event.type == SDL_KEYDOWN) {
				switch (event.key.keysym.sym) {
				case SDLK_RIGHT:
				{
					box.x += 15;
					Rect box(box.x, 100, 100, 100);
					std::cout << "Right Arrow Pressed: " << box.x << std::endl;
					break;
				}
				case SDLK_LEFT:
				{
					box.x -= 15;
					Rect box(box.x, 100, 100, 100);
					std::cout << "Left Arrow Pressed: " << box.x << std::endl;
					break;
				}
				}
			}
		}
	}
	SDL_Quit();
	return 0;
}
