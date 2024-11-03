class TinhDiemChuyenCan:
    def __init__(self, student_id, student_name, student_classname):
        self.student_id = student_id
        self.student_name = student_name
        self.student_classname = student_classname

    def cal(self, s: str):
        m = s.count('m')
        v = s.count('v')
        self.cc = max(0, 10 - m - v * 2)

    def __str__(self) -> str:
        return f'{self.student_id} {self.student_name} {self.student_classname} {self.cc} ' + ('KDDK' if self.cc == 0 else '')


a = {}
n = int(input())
for i in range(n):
    x = TinhDiemChuyenCan(input(), input(), input())
    a[x.student_id] = x

for i in range(n):
    student_id, s = input().split()
    a[student_id].cal(s)

for i in a:
    print(a[i])

'''
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
'''
