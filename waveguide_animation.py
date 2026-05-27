import numpy as np
import sys

if not hasattr(np, "float_"):
    np.float_ = np.float64
if not hasattr(np, "int_"):
    np.int_ = np.int64
if not hasattr(np, "asfarray"):

    np.asfarray = lambda x, **kwargs: np.array(x, dtype=np.float64, **kwargs)
# Meep과 최신 Numpy 간의 호환성 이슈 해결을 위한 패치 (np.float_ 및 np.int_ 정의)

import meep as mp
import gdsfactory as gf
import gplugins.gmeep as gm
import matplotlib.pyplot as plt
from gdsfactory.generic_tech import get_generic_pdk

# 1. PDK 활성화
get_generic_pdk().activate()
# 해당 PDK의 경우 물리적인 파라미터 값이 포함이 되어있음(도파로 두께, 빛의 굴절률 등등)

# 2. 컴포넌트 생성
c = gf.components.straight(length=10, width=0.5)
# 도파로의 값을 설정해주는 작업
# 현재 설정되어있는 값은 길이 10μm 0.5μm 폭을 가진 straight waveguide 즉 직선 도파로를 생성

# 3. 영역 확장
c = gf.add_padding_container(c, default=0, top=3, bottom=3)
# 해당 코드는 도파로 주변에 여백을 만들어 주는 작업
# 도파로 주변 evanescent field(소멸파) 관측 및 시뮬레이션 경계 조건(PML) 간섭 방지를 위해 상하 3μm 여백 추가

# 4. Meep 셋팅
print("setting")
sim_results = gm.get_simulation(
    component=c,
    resolution=20,
    is_3d=False,
)
# 해당 코드의 경우에는 Meep 의 시뮬레이션 환경 설정
# 여기서 resolution=20 은 1μm 당 격자를 20개 쪼갠다는 뜻 시간 절약을 위하여 3d는 구현을 현재 에정이 안되어있음
# 추후에 모든 프로젝트가 끝나면 업데이트를 해볼 예정

sim = sim_results['sim']

fig = plt.figure(figsize=(10, 5))
animate = mp.Animate2D(sim, fields=mp.Ez, f = fig, realtime=False, normalize=True)
# 해당 코드는 시뮬레이션 시각화를 위한 코드이다
# 여기서 봐야 할 내용중 하나는 바로 fields 에 mp.Ez 인데 이건 내가 전기장의 z축 성분을 보겠다 라는 선언
# 왜 Z축인가? 
# 맥스웰 방정식중 패러데이, 앙페르-맥스웰 법칙 에 의거, 전자기파의 진행 방향(x)과 전기장/자기장은 서로 수직임.
# 2D TE 모드 시뮬레이션에서는 전기장이 z축으로 진동하며 전파되므로, Ez 성분을 관측해야 파동의 전파 양상을 시각화할 수 있음.

# 5. 시뮬레이션 실행 
sim.run(mp.at_every(1, animate), until=200)

filename = "waveguide.gif"
animate.to_gif(10, filename)

print("완성")