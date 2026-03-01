#import系は最初にまとめておくと楽です。
import random
import time
print("＝＝＝ 運ゲー3連単 ＝＝＝")
#ランダムに出力するレース名のリストです。（カスタム可能）
race=["京都11R ミニマイルチャンピオンシップ（芝1600m）","阪神11R ミニ大阪杯（芝2000m）","東京11R ミニジャパンカップ（芝2400m）","中山11R ミニ有馬記念（芝2500m）","大井11R ミニ東京大賞典（ダ2000m）"]
print(random.choice(race))
print("ーーー 出馬表 ーーー")
#ランダムに出力する競走馬名のリストです。（カスタム可能）
horse=["イクイノックス","ウシュバテソーロ","エフフォーリア","クロノジェネシス","グランアレグリア","コントレイル","シャフリヤール","ジャックドール","スターズオンアース","セリフォス","ソダシ","タスティエーラ","タイトルホルダー","ダノンザキッド","デアリングタクト","ドウデュース","ドゥラエレーデ","べラジオオペラ","パンサラッサ","リバティアイランド",]
selected_horse=random.sample(horse,4)
#ここで順番に数字が振られるようにして、馬番として表示しています。
for i, horse in enumerate(selected_horse,start=1):
    print(f"{i} - {horse}")
print("ーーーーーーーーーー")
number_1=int(input("特に何も考えずに3連単を一点買いしましょう！\n" "1～4番の中で、1着になると思う馬番を半角で入力してください:"))
number_2=int(input("1～4番の中で、すでに選んだ馬番以外から、2着になると思う馬番を半角で入力してください:"))
number_3=int(input("1～4番の中で、すでに選んだ馬番以外から、3着になると思う馬番を半角で入力してください:"))
#inputでそれぞれ入力された数値は一つの変数としてまとめておきます。
user_numbers=[number_1, number_2, number_3]
buy=int(input("購入金額を半角で入力してください:"))
print(number_1,"→",number_2,"→",number_3,"の３連単を",buy,"円購入しました！\r\n")
#time.sleep(秒数)で指定した秒数後に次へと進むようにできます。
time.sleep(2)
print("スタートしました！！\n""レースの結果は...\r\n")
time.sleep(2)
#着順をランダムに決定します。
rankings=random.sample(range(1, 5), 3)
for i, num in enumerate(rankings, start=1):
    print(f"{i}着：{num}")
print("ーーーーーーーーーー")
#着順を3連単風に表示し、そのオッズをまたまたランダムで決定します。
arrow_format=' → '.join(map(str, rankings))
random_integer=random.randint(10,100000)
print("3連単:",arrow_format,"オッズ:",random_integer,"倍\r\n")
#入力された予想の馬番と着順が完全に合っているかどうかを判断して、結果を出力します。
if user_numbers==rankings:
    print("3連単的中おめでとうございます！ 払戻金は",buy*random_integer,"円です！")
else:
    print("残念...またチャレンジしてくださいね")