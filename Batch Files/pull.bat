:: Display each line of the batch file.
@ECHO ON

:: pull.bat file

:: Navigate to the correct directory in the command prompt
echo https://github.com/bustr003/SEISMessageBuilder.git
cd "C:\Users\Mhea Bustria\Desktop\SEISMessageBuilder"
git pull
git add .

:: Keep the command prompt open to accept more commands.
cmd