
## 개발환경 구축하기



1. 32bit python 설치를 위한 환경변수 등록
```
set CONDA_FORCE_32BIT=1
```
```
echo %CONDA_FORCE_32BIT%
```

2. Conda로 가상환경 생성하기 (파이썬 3.8) 
```
conda create -n moneymaker python=3.8
```

3. Conda 가상환경 활성화
```
conda activate moneymaker
```

4. Jupyther Notebook 사용을 위한 ipykernel 설치
```
pip install ipykernel
```

4. Jupyter Notebook 에 가상환경 등록
```
python -m ipykernel install --user --name moneymaker --display-name "Python (moneymaker)"
```

5. pyqt5, pyqtwebengine 설치
```
pip install pyqt5==5.12.1 pyqtwebengine==5.12.1
```

- (옵션) 가상환경 파일로 내보내기[특정 가상환경 활성화 이후]
```
conda env export > environment.yaml
```
- (옵션) 가상환경 파일로부터 가져오기
```
conda env create --file environment.yaml
```

