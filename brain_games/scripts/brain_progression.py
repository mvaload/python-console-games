#!/usr/bin/env python

from brain_games.src.games.progression import DESCRIPTION, run_game
from brain_games.src import engine


def main():
    engine.run(run_game(), DESCRIPTION)


if __name__ == '__main__':
    main()
