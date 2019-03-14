#include "pch.h"
#include<iostream>
#include "SDL.h"
#include "SDL_image.h"


SDL_Window * window = nullptr;
SDL_Surface * surface = nullptr;
SDL_Renderer * rend = nullptr;
SDL_Texture * text = nullptr;

const int Window_Width = 500;
const int Window_Height = 300;

void Init() {
	window = SDL_CreateWindow("SDL", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, Window_Width, Window_Height, SDL_WINDOW_RESIZABLE);
}

class Rect {
public:
	SDL_Renderer * rend = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
	int PosX, PosY, VelY = 0;
	SDL_Rect rect;

	Rect(int x, int y) {
		PosX = x;
		PosY = y;
	}

public:

	void up() {
		VelY -= 25;
		VelY *= 0.9;
	}

		void gravity() {
			if (PosY > Window_Height - 25) {
				VelY = 0;
			}
			else {
				VelY += 2;
				VelY *= 0.9;
				PosY += VelY;
				std::cout << VelY << std::endl;
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
	Rect box(80,30);
	SDL_Event  event;
	bool running = true;
	while (running == true) {
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = false;
			}
			if (event.key.keysym.sym == SDLK_UP) box.up();
		}
		SDL_Delay(15);
		box.gravity();
		box.move();
}
	std::cout << SDL_GetError();
	Quit();
	return 0;
}
