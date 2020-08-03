#!/usr/bin/bash
#---------------------------
# Writed By WitBlack HAcker
#---------------------------
#💬 Telegram:
#Https://t.me/WitBlack_ch
#
#💻 Web:
#Https://BugZone.ir
#
#📹 YouTube:
#https://www.youtube.com/channel/UCIgk2ldVeelyaHW3s4UkIIg (WitBlack)
#
#🎥 Aparat:
#Https://aparat.com/WitBlack
#
#⌨️ Github:
#Https://github.com/WitBlack
#
#📧 E-Mail:
#admin@bugzone.ir
#
#💬 Telegram:
#Https://t.me/WitBlack_ch
#
#💻 Web:
#Https://BugZone.ir
#
#📹 YouTube:
#https://www.youtube.com/channel/UCIgk2ldVeelyaHW3s4UkIIg (WitBlack)
#
#🎥 Aparat:
#Https://aparat.com/WitBlack
#
#⌨️ Github:
#Https://github.com/WitBlack
#
#📧 E-Mail:
#admin@bugzone.ir
#Powered By WitBlack Hacker
#Version 1.0.2 - Meli Code Generator
#
#💬 Telegram:
#Https://t.me/WitBlack_ch
#
#💻 Web:
#Https://BugZone.ir
#
#📹 YouTube:
#https://www.youtube.com/channel/UCIgk2ldVeelyaHW3s4UkIIg (WitBlack)
#
#🎥 Aparat:
#Https://aparat.com/WitBlack
#
#⌨️ Github:
#Https://github.com/WitBlack
#
#📧 E-Mail:
#admin@bugzone.ir
#
if [[ $EUID -ne 0 ]]; then
   echo "Please Run Script As Root User." ;
   exit 1;
fi
COD=0;
mkdir /tmp/No-IT-Forensic-Medicine_Installer > /dev/null;
cd /tmp/No-IT-Forensic-Medicine_Installer;
touch ERRORS;
apt-get install git -y > /dev/null
git clone https://github.com/witblack/No-IT-Forensic-Medicine.git 2> /dev/null 1> ERRORS;
ERRORS=$(cat ERRORS);
if [$ERRORS == ''];
then
	python -V 2> /dev/null 1> ERRORS;
	ERRORS=$(cat ERRORS);
	if [$ERRORS != ''];
	then
		echo 'Installing "python" package.';
		apt-get install -y python > /dev/null;
	else
		chmod +x No-IT-Forensic-Medicine/libs/getText.py;
		python No-IT-Forensic-Medicine/libs/getText.py && apt-get install -y python > /dev/null;
	fi
	echo 'Installing deepends.';
	apt-get install -y pip > /dev/null;
	pip install shutil > /dev/null;
	pip install os > /dev/null;
	pip install time > /dev/null;
	pip install termcolor > /dev/null;
	pip install str > /dev/null;
	mv No-IT-Forensic-Medicine/No-IT-Forensic-Medicine.py /usr/bin/no-it-forensic-medicine;
        chmod +x /usr/bin/no-it-forensic-medicine;
        echo 'Installed Successfully. Command: no-it-forensic-medicine';
else
        echo 'Error Connect To GitHub.com!';
	echo '';
	echo 'May Be:';
	echo '		[*] May be "git" package not fully installed.';
	echo '		[*] May be your internet connection lost or not connected.';
        COD=1;
fi
rm -r /tmp/No-IT-Forensic-Medicine_Installer > /dev/null;
exit $COD;
