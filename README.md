# **Photonic-Waveguide-Simulation**
**Meep** 와 **Gdsfactory** 파이썬 모듈을 이용하여 도파로 구현 및 시뮬레이션 

# **Straight Waveguide Analysis**
이 프로젝트는 직선 도파로에서 기본적인 빛의 전파를 시연하는 프로젝트 입니다.

# **Key Features**
**Standard Physical Design(현실적인 공정 반영)**: 시뮬레이션의 **현실성**을 위해 실제 반도체 공정 파라미터가 포함된 표준 **PDK**를 기반으로 설계하였습니다.

**Electromagnetic Field Analysis(전자기학적 분석)** : 맥스웰 법칙(페러데이,앙페르-맥스웰)에 근거하여 **Ez** 성분을 분석함으로써, 도파로 내부의 빛의 파동을 시각화 하였습니다. 

**Stable Simulation Flow(데이터 신뢰성 확보)** : 일시적인 과도 응답이 사라지고 정상 상태에 도달할 수 있도록 충분한 시뮬레이션 시간을 **until = 200**을 부여하여 데이터의 정확도를 높였습니다.

# **Simulation Result**
![Waveguide Animation](./waveguide.gif)

# **Requirements**
- `Meep`
- `gdsfactory`
- `gplugins`
