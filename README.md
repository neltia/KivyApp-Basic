# KivyApp-Basic
파이썬 Kivy 라이브러리로 만든 기본 앱 예제. Android를 기준으로 키비 예제를 설명한다.
<br>만든 이: Github/neltia, [@dsz08082](https://blog.naver.com/dsz08082)

<center><img src="https://postfiles.pstatic.net/MjAyMDA4MDdfMjg3/MDAxNTk2Nzg3MzIzODYw.IEamQ7iA3e533TMznG-lZbZuEzSFPLENkbGQzF1RdQAg.1a5ggmjjRHz1wT6jaHPJX_pRiX04sUD0npx_GorC6cYg.PNG.dsz08082/image.png?type=w773"></center>

## Welcome Kivy
키비 : Kivy, 크로스 플랫폼 사용자 인터페이스의 신속한 개발을 위한 오픈 소스 파이썬 라이브러리다. 
- 키비 응용 프로그램을 사용하면 리눅스, 윈도우에 사용하는 GUI 프로그램뿐 아니라 안드로이드, IOS 용도로 개발할 수 있다. 
- 그래픽 : 네이티브 위젯이 아닌 OpenGL ES 2를 통해 렌더링되어 운영체제 전반에 걸쳐 모양이 균일하다.
- 라이센스 : MIT 라이센스 아래 무료로 사용할 수 있고 전문적으로 지원을 받는다.

### Kivy Install
Windows
```
pip install --upgrade pip wheel setuptools
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/
pip install kivy
```

Linux
```
sudo apt-get update
sudo git clone https://github.com/kivy/kivy
sudo apt-get install python-kivy
sudo apt-get install python-kivy-examples
```

### Kivy Issue
kivy 실행화면에서 마우스 우클릭시 깨지는 이슈 방지
- python file 초반부에 다음 코드 추가
```
from kivy.config import Config

# 마우스 멀티터치 비활성
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
```
***
## Kivy Build
불도저(buildozer)를 사용해 파이썬 키비로 작성된 코드를 안드로이드 앱 패키킹
* buildozer는 윈도우 환경을 완벽히 지원하지 않으며 리눅스 환경을 사용해야 한다.

### Kivy Build Information
[키비 앱 빌드를 위한 가상머신 다운로드](https://drive.google.com/file/d/1LO2D1UBjRMzzkJKId5xW-gLS_2dQxxXM/view?usp=sharing)
- 가상머신: VirtualBox
- 운영체제: Linux Ubuntu 20.04
- 사용언어: Python3 kivy & Python3 venv
- 계정정보: (user01 / test1234)

### Kivy Build Setting
설명자료 : [Link](https://blog.naver.com/dsz08082/222068122443)
```
cd kiv
source my_env/bin/activate
export PATH=$PATH:~/.local/bin/
cd Downloads
gedit main.py
buildozer init
sudo apt update
buildozer -v android debug
```
