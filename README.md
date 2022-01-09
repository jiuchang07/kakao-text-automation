# kakao-text-automation
카카오톡 플러스친구로 학부모에게 학생의 등원, 단어, 하원 문자를 자동으로 보낼 수 있는 프로그램

# 모듈 설치 스크립트
opencv 모듈을 설치하지 않으면 confidence 관련 오류가 납니다.
```
pip install opencv-python
pip install pyperclip
pip install pyautogui
```
# 사전 준비
Editor ``python name_ID_editor.py``로 학생 이름과 ID를 잇는 ``python name_ID_dict.py``에 문자를 보낼 모든 학생을 등록한다. 
등록을 완료한 dictionary는 공유할 수 있다. 

# 실행 스크립트
```
python sender.py
```
# Google Sheets에서 주의할 점
- 단어시험은 반드시 'Vocab 1st' column에 ##/##의 형식으로 적는다. 
- check in/out time은 ##:##의 형식으로 적는다. 실수로 ; 를 사용하지 않도록 유의한다. 
- 첫번째 column에서 날짜를 제대로 입력한다.
- 가장 최근의 한 주만 보낼 수 있다. 
# 기타 주의할 점
- 화면에 반드시 search_icon.png가 보여야 한다. 
