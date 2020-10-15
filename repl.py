import code
import character
import pickle

def test_function():
    print("I am a test")
banner="""

   _____ _                   __           _ __       
  / ___/(_)___  ____ ___  __/ /___ ______(_) /___  __
  \__ \/ / __ \/ __ `/ / / / / __ `/ ___/ / __/ / / /
 ___/ / / / / / /_/ / /_/ / / /_/ / /  / / /_/ /_/ / 
/____/_/_/ /_/\__, /\__,_/_/\__,_/_/  /_/\__/\__, /  
             /____/                         /____/   

"""

def load_character(fname):
    with open("saves/"+fname, 'rb') as f:
        return pickle.load(f)

code.interact( banner=banner, local=locals())

print("The End.")