import warnings
warnings.filterwarnings('ignore', message='.*https://github.com/urllib3/urllib3/issues/3020.*') # annoying warning and doesnt really do anything

try:
  import requests
except ImportError:
  subprocess.call(['python3', '-m', 'pip install requests'])


import os, sys, time, subprocess
import requests, json, shutil, glob


def getkey(): # Credit to https://stackoverflow.com/a/1840
    import sys, tty, termios, select
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    answer = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return answer


# Initialize Data Directory

datapath = os.path.expanduser('~') + '/Library/Application Support/sdhEmily.RobloxPatcher'
escdatapath = os.path.expanduser('~') + '/Library/Application\ Support/sdhEmily.RobloxPatcher'
robloxapp = '/Applications/Roblox.app/Contents' # to be removed
if not os.path.exists(datapath):
  os.makedirs(datapath)
if not os.path.exists(datapath + '/Modifications'):
  os.makedirs(datapath + '/Modifications')
if not os.path.exists(datapath + '/FastFlags'):
  os.makedirs(datapath + '/FastFlags')
if not os.path.exists(datapath + '/applied.json'):
  settingsdict = {
    'rmbeta': False,
    'olddeath': False,
    'modsapplied': False,
    'fflagsapplied': False
}
  jsonfile = json.dumps(settingsdict, indent=1)
  os.chdir(datapath)
  with open('applied.json', 'w') as outfile:
    outfile.write(jsonfile)


config = json.load(open(datapath + '/applied.json'))

def exec(cmd, args, path=None, sh=False):
  if path != None:
    subprocess.call([cmd, args, path], shell=sh)
  else:
    subprocess.call([cmd, args], shell=sh)



# Menu Sections

def mainmenu():
  exec('clear', '.')
  print(' ___     _    _         ___      _      _            \n| _ \___| |__| |_____ _| _ \__ _| |_ __| |_  ___ _ _ \n|   / _ \ \'_ \ / _ \ \ /  _/ _` |  _/ _| \' \/ -_) \'_|\n|_|_\___/_.__/_\___/_\_\_| \__,_|\__\__|_||_\___|_|\n')
  print('Roblox.app Selected: /' + robloxapp.strip('/Contents') + '\n')

  print ('1) Utilities \n2) Mods\n3) FastFlags\n4) Select Roblox.app\n5) Quit\n')
  print('Waiting for input...')
  answer=getkey()
  if '1' in answer: utilities()
  elif '2' in answer: mods()
  elif '3' in answer: fflags()
  elif '4' in answer: chooseapp()
  elif '5' in answer: exit()
  elif answer:
    print('Please enter a valid number.')
    time.sleep(1) 
    mainmenu()

def utilities():
  global mobileapplied
  global olddeathapplied

  if os.path.exists(robloxapp + '/Resources/ExtraContent/places/oldMobile.rbxl'):
    mobileapplied = '[APPLIED]'
  else:
    mobileapplied = ''

  if os.path.exists(robloxapp + '/Resources/content/sounds/oldouch.ogg'):
    olddeathapplied = '[APPLIED]'
  else:
    olddeathapplied = ''

  exec('clear', '.')
  print(' _   _ _   _ _ _ _   _        \n| | | | |_(_) (_) |_(_)___ ___\n| |_| |  _| | | |  _| / -_|_-<\n \___/ \__|_|_|_|\__|_\___/__/\n')


  print ('1) Disable the Mobile main menu ' + mobileapplied, '\n2) Restore the old death sound ' + olddeathapplied, '\n3) Go back\n')
  print('Waiting for input...')
  answer=getkey()
  if '1' in answer: mobilemenu()
  if '2' in answer: oldoof()
  if '3' in answer: mainmenu()
  elif answer: 
    print('Please enter a valid number.')
    time.sleep(1) 
    utilities()

def mods():
  exec('clear', '.')
  print(' __  __         _    \n|  \/  |___  __| |___\n| |\/| / _ \/ _` (_-<\n|_|  |_\___/\__,_/__/\n')
  print ('1) Open mods folder\n2) Apply mods\n3) Remove mods\n4) Go back\n')
  print('Waiting for input...')

  answer=getkey()
  if '1' in answer: openmfolder()
  if '2' in answer: installmods()
  if '3' in answer: removemods()
  if '4' in answer: mainmenu() 
  elif answer: 
    print('Please enter a valid number.')
    time.sleep(1) 
    mods()

def fflags():
  exec('clear', '.')
  print(' ___        _   ___ _              \n| __|_ _ __| |_| __| |__ _ __ _ ___\n| _/ _` (_-<  _| _|| / _` / _` (_-<\n|_|\__,_/__/\__|_| |_\__,_\__, /__/\n                          |___/\n')

  print ('1) Open FastFlags folder\n2) Import JSON\n3) Apply FastFlags\n4) Remove FastFlags\n5) Go back\n')
  print('Waiting for input...')
  answer=getkey()
  if '1' in answer: openffolder()
  if '2' in answer: importjson()
  if '3' in answer: installfflags()
  if '4' in answer: removefflags()
  if '5' in answer: mainmenu() 
  elif answer: 
    print('Please enter a valid number.')
    time.sleep(1) 
    fflags()


# Utilities Functions

def mobilemenu():
  if os.path.exists(robloxapp + '/Resources/ExtraContent/places/oldMobile.rbxl'):
    global mobileapplied
    os.rename(robloxapp + '/Resources/ExtraContent/places/oldMobile.rbxl', robloxapp + '/Resources/ExtraContent/places/Mobile.rbxl')
    if os.path.exists(robloxapp + '/oldResources/ExtraContent/places/oldMobile.rbxl'):
      os.rename(robloxapp + '/oldResources/ExtraContent/places/oldMobile.rbxl', robloxapp + '/oldResources/ExtraContent/places/Mobile.rbxl')
    config['rmbeta'] = False
    saveconfig()
    mobileapplied = ''
    utilities()
  else:
    os.rename(robloxapp + '/Resources/ExtraContent/places/Mobile.rbxl', robloxapp + '/Resources/ExtraContent/places/oldMobile.rbxl')
    if os.path.exists(robloxapp + '/oldResources/ExtraContent/places/Mobile.rbxl'):
      os.rename(robloxapp + '/oldResources/ExtraContent/places/Mobile.rbxl', robloxapp + '/oldResources/ExtraContent/places/oldMobile.rbxl')
    config['rmbeta'] = True
    saveconfig()
    mobileapplied = '[APPLIED]'
    utilities()

def oldoof():
  if os.path.exists(robloxapp + '/Resources/content/sounds/oldouch.ogg'):
    global olddeathapplied
    os.remove(robloxapp + '/Resources/content/sounds/ouch.ogg')
    os.rename(robloxapp + '/Resources/content/sounds/oldouch.ogg', robloxapp + '/Resources/content/sounds/ouch.ogg')
    if os.path.exists(robloxapp + '/oldResources/content/sounds/oldouch.ogg'):
      os.remove(robloxapp + '/oldResources/content/sounds/ouch.ogg')
      os.rename(robloxapp + '/oldResources/content/sounds/oldouch.ogg', robloxapp + '/oldResources/content/sounds/ouch.ogg')
    olddeathapplied = ''
    config['olddeath'] = False
    saveconfig()
    utilities()
  else:
    os.rename(robloxapp + '/Resources/content/sounds/ouch.ogg', robloxapp + '/Resources/content/sounds/oldouch.ogg')
    exec('clear', '.')
    print('ℹ️  Downloading old death sound, please wait...\n')
    dl = requests.get('https://github.com/sdhEmily/RobloxPatcher/raw/main/ouch.ogg', allow_redirects=True)
    if os.path.exists(robloxapp + '/oldResources'):
      if os.path.exists(robloxapp + '/oldResources/content/sounds/oldouch.ogg'):
        os.rename(robloxapp + '/oldResources/content/sounds/ouch.ogg', robloxapp + '/oldResources/content/sounds/oldouch.ogg')
        open('/Applications/Roblox.app/Contents/oldResources/content/sounds/ouch.ogg', 'wb').write(dl.content)
    open('/Applications/Roblox.app/Contents/Resources/content/sounds/ouch.ogg', 'wb').write(dl.content)
    olddeathapplied = '[APPLIED]'
    config['olddeath'] = True
    saveconfig()
    print('\n✅  Successfully installed old death sound!')
    print('\nPress any key to return to the menu.')
    if not getkey():
      time.sleep()
    utilities()


# Mods Functions

def openmfolder():
  exec('open', datapath + '/Modifications')
  mods()

def installmods():
  exec('clear', '.')
  print('ℹ️  Applying mods, please wait...\n')
  if os.path.exists(robloxapp + '/oldResources'):
    shutil.rmtree(robloxapp + '/Resources')
    os.rename(robloxapp + '/oldResources', robloxapp + '/Resources')
  shutil.copytree(robloxapp + '/Resources', robloxapp + '/oldResources')
  shutil.copytree(datapath + '/Modifications', robloxapp + '/Resources', dirs_exist_ok=True)
  shutil.rmtree(datapath + '/Resources')
  print('✅ Successfully applied mods')
  config['modsapplied'] = True
  saveconfig()
  print('\nPress any key to return to the menu.')
  if not getkey():
    time.sleep()
  mods()

def removemods():
  exec('clear', '.')
  print('ℹ️  Removing mods, Please wait...\n')
  if os.path.exists(robloxapp + '/oldResources'):
    shutil.rmtree(robloxapp + '/Resources')
    os.rename(robloxapp + '/oldResources', robloxapp + '/Resources')
  config['modsapplied'] = False
  saveconfig()
  print('ℹ️  Successfully removed mods')
  print('\nPress any key to return to the menu.')
  if not getkey():
    time.sleep()
  mods()


# FastFlags Functions

def openffolder():
  exec('open', datapath + '/FastFlags')
  fflags()

def installfflags():
  exec('clear', '.')
  print('ℹ️  Applying FastFlags, please wait...\n')
  os.chdir(datapath + '/FastFlags/')
  finaljson = {}
  for f in glob.glob('*.json'):
      with open(f, 'r', encoding='utf-8') as infile:
        file_content = json.load(infile)
        for key, value in file_content.items():
          finaljson[key] = value
  jsonfile = json.dumps(finaljson, indent=1)
  if os.path.exists(robloxapp + '/MacOS/ClientSettings'):
    shutil.rmtree(robloxapp + '/MacOS/ClientSettings')
    os.makedirs(robloxapp + '/MacOS/ClientSettings')
  else:
    os.makedirs(robloxapp + '/MacOS/ClientSettings')
  os.chdir(robloxapp + '/MacOS/ClientSettings')
  with open('ClientAppSettings.json', 'w') as outfile:
    outfile.write(jsonfile)
  config['fflagsapplied'] = True
  saveconfig()
  print('✅ Successfully applied FastFlags')
  print('\nPress any key to return to the menu.')
  if not getkey():
    time.sleep()
  fflags()

def removefflags():
  exec('clear', '.')
  print('ℹ️  Removing FastFlags, please wait...\n')
  if os.path.exists(robloxapp + '/MacOS/ClientSettings'):
    shutil.rmtree(robloxapp + '/MacOS/ClientSettings')
  config['fflagsapplied'] = False
  saveconfig()
  print('✅ Successfully removed FastFlags!')
  print('\nPress any key to return to the menu.')
  if not getkey():
    time.sleep()
  fflags()

def importjson():
  lines = []
  exec('clear', '.')
  print('Paste the JSON you want to import below:\n')
  while True:
    importing = input()
    if importing == '':
      break
    else:
      lines.append(importing + '\n')
  try:
    json.loads(''.join(lines))
  except ValueError as error:
    exec('clear', '.')
    print('⚠️  An error occured imporitng this JSON!')
    print(error)
    print('\nPress any key to return to the menu.')
    if not getkey():
      time.sleep()
    fflags()
  def savejson():
    exec('clear', '.')
    name = input('What do you want to name this JSON? > ')
    if not os.path.exists(datapath + '/FastFlags/' + name + '.json'):
      os.chdir(datapath + '/FastFlags/')
      with open(name + '.json', 'w') as outfile:
        outfile.write(''.join(lines))
      print('\n✅ Successfully saved ' + name + '.json')
      print('\nPress any key to return to the menu.')
      if not getkey():
        time.sleep()
      fflags()
    else:
      print('\n⚠️  File already exists. Please try another name.')
      time.sleep(1)
      savejson()
  savejson()

# Extra functions

def saveconfig():
  jsonfile = json.dumps(config, indent=1)
  os.chdir(datapath)
  with open('applied.json', 'w') as outfile:
    outfile.write(jsonfile)


# Load the main menu or start firestrap

mainmenu()