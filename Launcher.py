from Script.ScriptRunner import ScriptRunner
import os


if __name__ == "__main__":
    script = ScriptRunner()
    script.prep()
    script.run()
    script.show_results()
