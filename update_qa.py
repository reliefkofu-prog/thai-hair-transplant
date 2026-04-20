import re
import os

cases_path = "/Users/satoseiya/Desktop/AG/タイ植毛/cases.html"
with open(cases_path, "r", encoding="utf-8") as f:
    cases = f.read()

cases = re.sub(r'\s*<div class="category-tabs">.*?</div>', '', cases, flags=re.DOTALL)
cases = re.sub(r'\s*<p class="card-text">.*?</p>', '', cases, flags=re.DOTALL)

with open(cases_path, "w", encoding="utf-8") as f:
    f.write(cases)

price_path = "/Users/satoseiya/Desktop/AG/タイ植毛/flow.html"
with open(price_path, "r", encoding="utf-8") as f:
    price_content = f.read()

qa_html = """
    <!-- よくある質問（Q&A） -->
    <section class="section">
        <div class="container">
            <h2 class="section-headline">よくある質問（Q&A）</h2>
            <div class="faq-list">
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q1 植毛手術は痛いですか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        手術は局所麻酔で行うため、施術中の痛みはほとんどありません。麻酔の注射の際に少しチクっとした痛みがありますが、その後は痛みを感じることはほとんどありません。痛みを感じるときには遠慮なくスタッフに伝えてください。麻酔薬や鎮痛薬を状態にあわせて調整いたします。術後は軽い違和感や腫れが出る場合がありますが、多くの場合は数日で落ち着きます。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q2 何日くらいの滞在が必要ですか？帰国はいつできますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        一般的には 2〜3日程度の滞在 で施術が可能です。<br>
                        【滞在例】<br>
                        ・1日目：タイ到着・ホテルチェックイン<br>
                        ・2日目：術前カウンセリング・植毛手術<br>
                        ・3日目：術後チェックとケア・帰国<br>
                        手術翌日にクリニックで術後チェックと洗髪ケアを受けた後、帰国が可能です。余裕を持ちたい方は4〜5日程度滞在される方もいます。植毛は体への負担が少ない手術のため、多くの方が短期間の滞在で施術を受けています。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q3 手術後に観光はできますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        術後は移植した毛根を安定させるため、安静に過ごすことが推奨されています。長時間の外出は負担になるため、控えていただくと良いです。<br>
                        近くのショッピングモールでのお買い物や食事などをお勧めしております。日本食レストランや足裏マッサージなど楽しんでいただくことは可能です。<br>
                        多くの方はホテルでゆっくり過ごし、術後チェックとケアを受けて帰国されます。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q4 植毛した髪はどのくらいで生えてきますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        植毛した髪は、手術後すぐに伸び続けるわけではなく、一度抜けてから再び生えてくるという特徴があります。<br>
                        【一般的な経過の目安】<br>
                        ・2週間～2ヶ月前後：移植した髪と既存毛が抜ける時期（脱落やショックロスと呼ばれます）<br>
                        ・3〜4ヶ月：新しい髪の発毛が始まる時期<br>
                        ・6ヶ月：見た目の変化を感じる方が増える時期<br>
                        ・12ヶ月：完成に近い状態になる時期<br>
                        植毛後は個人差がありますが一部に脱毛が起きることがあります。この時期に関しては短期間とうこともあり、待つ期間だと考えてください。脱毛も正常な毛髪サイクルになる準備段階ですので、心配する必要はないです。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q5 植毛の効果は永続しますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        移植に使用する毛根は、後頭部など薄毛の影響を受けにくい部位から採取します。この毛根はDHT（薄毛の原因となるホルモン）の影響を受けにくい性質を持つため、移植後も抜けにくく、長期的な効果が期待できます。<br>
                        ただし、植毛した部分の周囲にある既存の毛については、薄毛が進行する可能性があります。そのため、フィナステリドやミノキシジルなどを併用し、薄毛の進行を抑えることを推奨する場合があります。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q6 植毛とAGA治療薬は何が違いますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        AGA治療薬（フィナステリド・ミノキシジルなど）は、これ以上薄毛を進行させない・現在の髪を維持・増やすことを目的とした治療です。一方、植毛はすでに薄くなった部分に毛根を移植し、髪を物理的に増やす施術です。<br>
                        「薬を飲んでいるが、薄くなった部分が気になる」「より早く見た目を改善したい」という方に、植毛は特に有効な選択肢となります。薬と植毛を併用するケースも多くあります。<br>
                        またAGA治療薬の効果は頭頂部に限定的であることが多く、効果がみられる年齢も若年層が多いです。そのため進行された薄毛に関しては植毛が適応となることが多いです。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q7 術後もAGA治療薬を飲み続ける必要がありますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        移植した毛根自体は薬なしでも維持されますが、周辺の既存毛の薄毛進行を抑えるために、術後も内服薬の継続をおすすめする場合があります。<br>
                        薬の継続については、医師カウンセリングの際に個別にご相談いただけます。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q8 植毛は周りにバレますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        術後数日間は個人差がありますが赤みや腫れが出ることがあります。ただ、髪を少し伸ばしておく・数日の有休取得などで、職場や家族に気づかれずに済んでいる方がほとんどです。<br>
                        個々の状態にあわせて、以下のような対策をご提案・サポートさせていただくことが多いです。<br>
                        ・髪の毛を少し長めに伸ばしておく<br>
                        ・帽子やウイッグを着用する<br>
                        ・バンダナを使用する<br>
                        ・渡航を含めて数日〜1週間程度の休暇を取る<br>
                        また、植毛後は直射日光は避ける必要があるため、クリニックからはバンダナの支給があり着用する方が多いです。カウンセリング時には、髪型やお仕事の状況に合わせて目立ちにくい方法やダウンタイムの過ごし方についてもご案内いたします。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q9 女性でも植毛は受けられますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        はい、女性の方も施術を受けることができます。女性の薄毛（びまん性脱毛・分け目の薄さ、頭頂部の薄さなど）でお悩みの方からのご相談も承っております。<br>
                        海外では女性の植毛も非常に多く実施されております。タイ植毛では周りの目を気にせずに植毛に専念することが可能あり、最新の需要は伸びております。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q10 植毛は何歳から受けられますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        一般的には20歳以上であれば施術可能です。ただし薄毛の進行状況によっては、医師から将来的なデザインを考慮した提案を行う場合があります。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q11 支払い方法を教えてください。</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        クリニックによって対応が異なります。現金（タイバーツ）のほか、クレジットカード（VISA・Mastercard）でのお支払いが可能です。<br>
                        ただし、クリニックによってはカード決済に手数料（約3%）が発生する場合があります。手数料が気になる方には、現金払いやカード手数料無料のクリニックもご案内いたしますので、カウンセリング時にお気軽にご相談ください。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q12 3つのクリニック、どう選べばよいですか ？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        それぞれのクリニックに特徴があります。<br>
                        ・費用をできるだけ抑えたい方 → Hair Restore（価格が最もリーズナブル、カード手数料無料）<br>
                        ・宿泊サポートも充実させたい方 → Full Hair（中級ホテル4泊無料など特典が手厚い）<br>
                        ・実績・安心感を最優先したい方 → DHT Clinic（本院としての豊富な実績）<br>
                        どのクリニックが合うかは、薄毛の状態・ご予算・ご希望によって異なります。無料オンラインカウンセリングでご状況をお伺いしたうえで、最適なクリニックをご提案いたします。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q13 日本語は通じますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        クリニックは英語対応ですが、相談・カウンセリング・手術当日のすべてに日本語通訳が対応いたします。言葉の壁を理由に迷う必要はありません。<br>
                        医療従事者（医師、薬剤師、看護師等）で語学が非常に堪能な通訳チームを構成しており、24時間対応も可能です。
                    </div>
                </details>
                <details style="margin-bottom: 16px; border: 1px solid var(--border-color); border-radius: 8px; background: #fff;">
                    <summary style="padding: 24px; font-weight: bold; cursor: pointer; font-size: 18px;">Q14 現地への同行サポートはありますか？</summary>
                    <div style="padding: 0 24px 24px 24px; color: var(--text-secondary); line-height: 1.8;">
                        現地までの渡航等不安な方には同行サポート（オプション）もご案内しております。同行サポートは、週末・ゴールデンウイーク・年末年始・お盆休みなどのタイミングで可能です。ご希望がございましたら遠慮なくご連絡ください。<br>
                        当日は医療に詳しい通訳スタッフが同行し、クリニックでのカウンセリングや手術当日のサポートを行います。同行費用はご負担いただきますが、複数名での参加を想定しているため、人数が集まることで比較的リーズナブルにご利用いただけます。
                    </div>
                </details>
            </div>
        </div>
    </section>
"""

new_price_content = price_content.replace('    <!-- CTA: まずは匿名相談、無料カウンセリングへ -->', qa_html + '\n    <!-- CTA: まずは匿名相談、無料カウンセリングへ -->')

with open(price_path, "w", encoding="utf-8") as f:
    f.write(new_price_content)

print("Done.")
