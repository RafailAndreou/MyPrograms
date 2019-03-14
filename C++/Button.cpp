#include "pch.h"
#include<iostream>
#include "SDL.h"
#include "SDL_image.h"


SDL_Window * window = nullptr;

const int Window_Width = 500;
const int Window_Height = 300;

void Init() {
	window = SDL_CreateWindow("SDL", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, Window_Width, Window_Height, SDL_WINDOW_RESIZABLE);
}


void Quit() {
		SDL_DestroyWindow(window);
		SDL_Quit();
}

class Rect {
	SDL_Renderer * olrend = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
	SDL_Rect outline;
	SDL_Rect rect;

public:
	Rect(int x, int y, int h, int w) {
		outline.x = x;
		outline.y = y;
		outline.h = h;
		outline.w = w;
		rect.x = x+1.25;
		rect.y = y+1.25;
		rect.h = h-2.5;
		rect.w = w-2.5;
		
	}
	void draw() {
		SDL_SetRenderDrawColor(olrend, 40, 40, 40,255);
		SDL_RenderFillRect(olrend, &outline);
		SDL_SetRenderDrawColor(olrend, 200, 200, 200, 255);
		SDL_RenderFillRect(olrend, &rect);
		SDL_RenderPresent(olrend);
	}
};

int main(int argc, char *argv[]) {
	Init();
	SDL_Event  event;
	Rect Button(0,0,30,90);
	bool running = true;
	Button.draw();
	while (running == true) {
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = false;
			}
		}
	}
	std::cout << SDL_GetError();
	Quit();
	return 0;
}
