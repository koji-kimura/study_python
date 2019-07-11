import subprocess
# ターミナルで実行したのと同じ結果が出てくる
# subprocess.run(['ls', '-al'])
# shell = Trueはセキュリティ的に実行しないほうがいい
# subprocess.run('ls -al | grep test', shell=True, check=True)

p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
