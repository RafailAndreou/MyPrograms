#include "pch.h"
#include<iostream>
#include "SDL.h"
#include "SDL_image.h"
#include<filesystem>
#include<string>

std::string filepath = "D://Delete2.png";
SDL_Window * window = nullptr;
SDL_Surface * surface = nullptr;
namespace fs = std::experimental::filesystem;
bool Init() {
	window = SDL_CreateWindow("Window", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 300, 200, SDL_WINDOW_RESIZABLE);
	if (window == nullptr) {
		std::cout << "Couldn't create window. Error: " << SDL_GetError();
		return false;
	}
	else {
		SDL_Surface * surface = SDL_GetWindowSurface(window);
		return true;
	}
}
void Load(){
	int imgFlags = IMG_INIT_PNG | IMG_INIT_JPG;
	if(IMG_Init(imgFlags!= imgFlags)) {
		std::cout << "Error: " << IMG_GetError() << std::endl;
	}
	else {
		std::cout << fs::current_path() << std::endl;
		surface = IMG_Load(filepath.c_str());
		if (!surface)
			std::cout << "Image couldn't load" << SDL_GetError();
		else
		std::cout << "Surface Loaded" << std::endl;
	}
}
void Quit() {

	SDL_DestroyWindow(window);
	SDL_Quit();
}

int main(int argc, char*argv[]) {
	bool running = true;
	SDL_Event event;
	Init();
	Load();
	while (running) {
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = false;
			}
		}
	
	}
	Quit();
	return 0;
}