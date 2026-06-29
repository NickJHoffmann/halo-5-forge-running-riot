import pydirectinput
import time
import click
import logging


def setup_logging() -> None:
    """Sets up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s",
        handlers=[logging.StreamHandler()],
    )


def _keystroke(key: str) -> None:
    """Presses a key down and then releases it."""
    pydirectinput.keyDown(key)
    time.sleep(0.15)  # Small delay to ensure the key press is registered
    pydirectinput.keyUp(key)


@click.command()
@click.argument("num_cycles", type=int, required=True)
@click.option(
    "--game-execution-time",
    type=int,
    default=30,
    help="Amount of time the game takes to execute, from clicking 'Start' to the carnage report screen.",
)
def main(num_cycles: int, game_execution_time: int) -> None:
    """Loop the game start process for a specified number of cycles."""
    setup_logging()
    logging.info(f"Starting the script with {num_cycles} cycles")
    logging.info(
        "Please make sure the game is open and active on the custom game launch screen, with the 'Privacy' menu option highlighted. The script will start in 10 seconds..."
    )
    time.sleep(10)

    for i in range(1, num_cycles + 1):
        logging.info(f"Starting cycle {i}/{num_cycles}...")

        # Press the arrow up key (after each game you are under "Privacy")
        _keystroke("up")
        logging.info("Pressed the arrow up key to go to Start")

        # Wait a few seconds before pressing enter
        time.sleep(2)

        # Press the Enter key to start the game
        _keystroke("enter")
        logging.info("Game started...")

        # Wait for the specified delay
        time.sleep(game_execution_time)

        # Press the esc key (after each game you are in the carnage report)
        _keystroke("esc")
        logging.info("Left the carnage report")

        logging.info(f"Completed cycle {i}/{num_cycles}")

        if i < num_cycles:
            logging.info("Waiting for 5 seconds before starting the next cycle...")
            time.sleep(5)


if __name__ == "__main__":
    main()
