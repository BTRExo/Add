o
    ��b�  �                	   @   s�  d dl mZ d dlmZ d dlZd dlZd dlmZmZ d dl	m
Z
 e�  ejZejZejZejZejZejZejZeeeeeegZzd dlZW n ey_   ee� de� �� e�d� Y nw dd	� Zd
d� Z	 e�  e�  eed e � eed e � eed e � eed e � eed e � e e!d��Z"e"dk�r'g Z#e$dd��oZ%e e!de� de� ���Z&e'e&�D ]!Z(e)e!de� de� ���Z*d�+e*�,� �Z-e�.e-ge%� e#�/e-� q�ede� d�� e�  ede� d�� e#D ]Z0ede0� �dd�Z1e1�2e0� ee� d�� e1�3�  q�e!d � W d  � n	1 �sw   Y  e%�4�  �n8e"d!k�r
g Z5g Z6e$dd"�Z7	 z
e5�/e�8e7�� W n
 e9�yJ   Y nw �q6e7�4�  e:e5�d k�rdeed# � e
d$� �n�e5D ]LZ;e)e;d  �Z<ede<� �d%d&�Z=e=�>�  e=�?� �s�ze=�@e<� eeA� d'e<� d(e� �� W �qf e�y�   eee)e<� d) e � e6�/e;� Y �qfw �qfe:e6�d k�r�eed* � e!d+� �n�e6D ]ZBe5�CeB� �q�e$dd,��ZDe5D ]Z"e"d  ZEe�.eEgeD� �q�W d  � n	1 �s�w   Y  eD�4�  eed- e � e!d+� �nUe"d$k�r�g ZFe$dd"�ZG	 z
eF�/e�8eG�� W n
 e9�y+   Y nw �qeG�4�  d Z(ee� d.�� eFD ]ZHee� d/e(� d0eHd  � e� �� e(d7 Z(�q=e e!de� d1e� ���ZIe)eFeI d  �Z<e<d2 ZJejKd3k�r|e�d4eJ� �� ne�d5eJ� �� eFeI= e$dd,�ZGeFD ]	Z;e�.e;eG� �q�ede� d6e� �� e!d+� eG�4�  n�e"d7k�rQede� d8�� ze�Ld9�ZMW n   ee� d:�� ee� d;�� eN�  Y eOeMjP�d<k�rEe)e!e� d=eMjP� d>e� ���ZQeQd?k�s�eQd@k�s�eQdAk�r9ee� dB�� ejKd3k�re�dC� e�dD� n
e�dE� e�dF� e�dG� e�dH� ee� dIeMjP� �� e!dJ� eN�  n&ee� dK�� e!dL� nee� dM�� e!dL� ne"dNk�r_e�  e�  eN�  qi)O�    )�TelegramClient)�PhoneNumberBannedErrorN)�init�Fore)�sleepz#[i] Installing module - requests...zpip install requestsc                  C   sH   dd l } g d�}|D ]}t| �t�� |� t� �� q
tdt� d�� d S )Nr   )uJ    ██████╗░███████╗██╗░░██╗ uJ    ██╔══██╗██╔════╝╚██╗██╔╝ uJ    ██████╔╝█████╗░░░╚███╔╝░ uJ    ██╔══██╗██╔══╝░░░██╔██╗░ uJ    ██║░░██║███████╗██╔╝╚██╗ uJ    ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝ z   Version: 1.0 | Author: REX�
)�random�print�choice�colors�n)r   �b�char� r   �%/storage/emulated/0/gjk/rexmanager.py�banner   s
   r   c                   C   s&   t jdkrt �d� d S t �d� d S )N�nt�cls�clear)�os�name�systemr   r   r   r   �clr+   s   
r   Tz[1] Add New Accountsz[2] Filter All Banned Accountsz[3] Delete specific accountsz[4] Update your Scriptz[5] Exitz
Enter Your Choice: �   zvars.txt�abr   z& [~] Enter number of accounts to add: z [~] Enter Phone Number: � z# [i] Saved all accounts in vars.txtz" [*] Logging in from new accounts
z	sessions/i�$ Z 7e14b38d250953c8c1e94fd7b2d63550u>   [+] 𝐋𝐨𝐠𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮Lz"
 Press enter to goto main menu...�   �rbz4[!] There are no accounts! Please add some and retry�   i�l{ Z 7d1e0295ee1c2628f1933e9ffd2d8b78z[+] z is not bannedz is banned!zCongrats! No banned accountsz!
Press enter to goto main menu...�wbz[i] All banned accounts removedz [i] Choose an account to delete
�[z] z[+] Enter a choice: z.sessionr   zdel sessions\zrm sessions/z[+] Account Deleted�   z[i] Checking for updates...zOhttps://raw.githubusercontent.com/krish775/Rex-TG-Member-Adder/main/version.txtz& You are not connected to the internetz) Please connect to the internet and retryg�������?z[~] Update available[Version z]. Download?[y/n]: �yZyes�Yz[i] Downloading updates...zdel rexadder.pyzdel rexmanager.pyzrm rexadder.pyzrm rexmanager.pyzZcurl -l -O https://raw.githubusercontent.com/krish775/Rex-TG-Member-Adder/main/rexadder.pyz\curl -l -O https://raw.githubusercontent.com/krish775/Rex-TG-Member-Adder/main/rexmanager.pyz[*] Updated to version: zPress enter to exit...z[!] Update aborted.z Press enter to goto main menu...z$[i] Your Astra is already up to date�   )RZtelethon.syncr   Ztelethon.errors.rpcerrorlistr   �pickler   Zcoloramar   r   �timer   ZRESETr   ZBLUEZlgZRED�rZWHITE�wZCYAN�cyZYELLOWZyeZGREENZgrr   Zrequests�ImportErrorr	   r   r   r   �int�input�aZnew_accs�open�gZnumber_to_add�range�i�strZphone_number�join�splitZparsed_number�dump�appendZnumber�c�startZ
disconnect�closeZaccountsZbanned_accs�h�load�EOFError�lenZaccountZphoneZclientZconnectZis_user_authorizedZsend_code_requestZblue�m�remove�kZPhoneZaccs�fZacc�indexZsession_filer   �get�version�exit�float�text�promptr   r   r   r   �<module>   s4   �



�

��

����

�� 










 ��