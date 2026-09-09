"""
量子テレポーテーションをQiskitで実装する｜状態を"転送"するしくみ

元記事: https://quantum.yurufuwa.work/learn/teleportation-qiskit
ゆるふわ量子コンピュータ (quantum.yurufuwa.work) の解説記事から抜粋したコードです。
"""

from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 3)   # q0=送る状態, q1=アリス, q2=ボブ
qc.h(0)
qc.t(0)                     # 何か特徴のある状態にしておく
qc.barrier()

qc.h(1)
qc.cx(1, 2)
qc.barrier()

qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)
qc.measure(1, 1)
qc.barrier()

with qc.if_test((qc.clbits[1], 1)):   # q1の測定が1ならX
    qc.x(2)
with qc.if_test((qc.clbits[0], 1)):   # q0の測定が1ならZ
    qc.z(2)

from qiskit_aer import AerSimulator

# ①の逆（T†→H）をq2にかけて測定
qc.tdg(2)
qc.h(2)
qc.measure(2, 2)

result = AerSimulator().run(qc, shots=1000).result()
counts = result.get_counts()

# q2（左端ビット）が常に0なら成功
q2_zero = sum(v for k, v in counts.items() if k[0] == "0")
print("q2=0 の割合:", q2_zero / 1000)   # 1.0 になる
