<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()


  const { data: article } = await useFetch(`${ config.public.baseURL }c/article/1/`)

  const relateds = ref([
    { "name": "Ручная дуговая сварка", "link": 8 },
    { "name": "Воздушно-плазменная резка", "link": 12 },
    { "name": "Аргонодуговая сварка", "link": 11 },
    { "name": "Механизмы подачи проволоки", "link": 99 },
    { "name": "Полуавтоматическая сварка", "link": 9 },
    { "name": "Автоматическая сварка", "link": 106 },
    { "name": "Электроды", "link": 14 },
    { "name": "Проволока", "link": 18 },
    { "name": "Прутки", "link": 23 },
  ])

</script>



<template>
  <div>
    <AppHeader />
    <AppNavbar />

    <div class="container mx-auto px-4 py-2 max-w-6xl lg:px-8">

      <div class="bg-white rounded-md border dark:border-gray-700 dark:bg-gray-800 shadow-md py-4 px-4">
        <div class="">

          <p class="text-xl">Виды:</p>
          <div class="my-6">
            <p class=""><u><span style="font-size:18px"><em><strong>Трансформаторные модели</strong></em></span></u> многие считают устаревшими, но с другой стороны у них самая простая конструкция. Техника выполняет преобразование входного напряжения до уровня в 50–90 вольт, которые используются в процессе сварки. К преимуществам этих моделей также относят долговечность, надежность и неприхотливость в обслуживании.</p>
            <div class="bq-article md:mx-2 my-6 lg:mx-8">
              <p class="">Минусы:</p>
              <p class="">
                Большая масса. Самые легкие модели весят 20 килограммов. Это связано с необходимостью наличия габаритного сердечника и использования проводов вторичной обмотки большого сечения, способных выдержать высокий ток. 
                На выходе трансформаторных моделей только переменный ток, что приводит к разбрызгиванию металла. Для уменьшения этого эффекта рекомендуется покупать только рутиловые или фтористо-кальциевые электроды диаметром до 2,5 миллиметров.
                Трансформаторы чувствительны к сетевому напряжению. Многие трансформаторные модели работают только от трехфазной сети.
              </p>
            </div>
          </div>

          <div class="my-6">
            <p class="">
              <u><span style="font-size:18px"><em><strong>Полуавтоматы</strong></em></span></u> можно отнести к списку узкоспециализированных устройств. По принципу работы и размерам их можно отнести к трансформаторным. Работают устройства не с электродами, а с проволокой. Одновременно подается инертный газ (углекислый, аргон, гелий). За счет этого достигается точность шва и стойкость к коррозии. 
            </p>
          </div>

          <div class="my-6">
            <p class="">
              <u><span style="font-size:18px"><em><strong>Выпрямители</strong></em></span></u>. Это компромиссное решение, которое находится между трансформаторными и продвинутыми инверторными аппаратами. Конструкция помимо трансформатора имеет выпрямительную схему, благодаря чему на выходе получается стабильный ток.
            </p>
            <div class="my-4">
              <p>
                Применение выпрямительного блока решило часть недостатков трансформаторной техники:
              </p>

              <ul class="mx-4 lg:mx-8 text-sm">
                <li class="li-article">Лучшее качество шва и возможность комфортной работы для новичков</li>
                <li class="li-article">Более широкий выбор электродов</li>
                <li class="li-article">Возможность комфортно варить чугун и цветные металлы</li>
              </ul>
            </div>


            <p class="">
              Несмотря на усовершенствования, часть недостатков перекочевала — это большой вес и высокая зависимость от входного тока и напряжения. При этом для многих покупателей будет ощутим прирост стоимости.
            </p>

          </div>

          <div class="my-10">
            <p>
              <u><span style="font-size:18px"><em><strong>Инверторные сварочные аппараты</strong></em></span></u>. Отличаются лучшими эксплуатационными характеристиками за счет усложнения схемы. Помимо выпрямителя, фильтра и трансформатора используется инвертор. Компонент формирует высокочастотный ток до 100 кГц, который фильтруется и выпрямляется на выходе. При увеличении частоты тока нужны меньшие габариты и масса трансформатора. Применение сложного преобразования сигнала в инверторных моделях дает аппаратам множество достоинств по сравнению с другими типами:
            </p>
          
            <ul class="mx-4 my-4 lg:mx-8 text-sm">
              <li class="li-article">Малый вес и габариты</li>
              <li class="li-article">Высокое качество дуги</li>
              <li class="li-article">Минимальное разбрызгивание металла</li>
              <li class="li-article">Энергетическая эффективность, что позволяет использовать аппараты даже в сетях 220 В</li>
            </ul>
            <p>
              Недостатком является сложная начинка, поэтому ремонт техники если и возможен, то крайне дорогостоящий.
            </p>
            <p>
              Рынок предлагает профессиональные и домашние инверторные сварочные аппараты, отличающиеся ценой и техническими характеристиками.
            </p>
          
            <div class="bq-article md:mx-2 my-6 lg:mx-8">
              <p>
                Инверторы подойдут как для новичков, так и для профессионалов. Подкатегорией являются бестрансформаторные модели. Они отличаются лучшей стабильностью дуги, меньшими энергозатратами в режиме холостого хода.
              </p>
            </div>


            <div class="relative">
              
              <div class="flex gap-4 my-4">
                <div class="border-b border-gray-300 group">
                  <p class="text-sm cursor-pointer">Продвинутые, для широкого круга пользователей <span class="mdi mdi-help-circle-outline"></span></p>
                  
                  <div class="absolute bottom-0 left-0 xl:left-auto transition invisible group-hover:visible opacity-0 group-hover:opacity-100 duration-500 ease-in-out group-hover:transform z-40 translate-y-0 group-hover:-translate-y-4">
                    <div class="grid grid-cols-1 md:flex items-center bg-white rounded-xl px-2 py-6 my-6 w-full md:w-[500px] border shadow-xl shadow-black/30">
                      <div class="flex lg:flex-none lg:w-[120px] justify-center">
                        <img src="/prod-img/invertor.webp" class="w-[120px]"/>
                      </div>
                      <div class="flex-1">
                        <div class="flex flex-col gap-4 items-center justify-center">
                          <p class="text-gray-700 px-4 py-4 text-sm">Активное широкое распространение инверторных технологий послужило появлению домашних и профессиональных сварочных агрегатов — можно выбирать для любых целей.</p>
                          <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                            <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg px-12 py-2">
                              <nuxt-link :to="{ name: 'prods', query: { ct: 8 } }" class="text-white text-base">Перейти в каталог</nuxt-link>
                            </div>
                          </div>
                        
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="border-b border-gray-300 group">
                  <p class="text-sm cursor-pointer">Для нечастого использования, новичкам <span class="mdi mdi-help-circle-outline"></span></p>
                  
                  <div class="absolute bottom-0 left-0 xl:left-auto transition invisible group-hover:visible opacity-0 group-hover:opacity-100 duration-500 ease-in-out group-hover:transform z-40 translate-y-0 group-hover:-translate-y-4">
                    <div class="grid grid-cols-1 md:flex items-center bg-white rounded-xl px-2 py-6 my-6 w-full md:w-[500px] border shadow-xl shadow-black/30">
                      <div class="flex lg:flex-none lg:w-[120px] justify-center">
                        <img src="/prod-img/invertor-third.webp" class="w-[120px]"/>
                      </div>
                      <div class="flex-1">
                        <div class="flex flex-col gap-4 items-center justify-center">
                          <p class="text-gray-700 px-4 py-4 text-sm">Выпрямители подойдут нетребовательным новичкам, которые не собираются часто прибегать к сварочным работам или заниматься этим профессионально.</p>
                          <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                            <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg px-12 py-2">
                              <nuxt-link :to="{ name: 'prods', query: { ct: 8 } }" class="text-white text-base">Перейти в каталог</nuxt-link>
                            </div>
                          </div>
                        
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="flex gap-4 my-4 ">
                <div class="border-b border-gray-300 group">
                  <p class="text-sm cursor-pointer">Для опытных пользователей <span class="mdi mdi-help-circle-outline"></span></p>
                  <div class="absolute bottom-0 left-0 xl:left-auto transition invisible group-hover:visible opacity-0 group-hover:opacity-100 duration-500 ease-in-out group-hover:transform z-40 translate-y-0 group-hover:-translate-y-4">
                    <div class="grid grid-cols-1 md:flex items-center bg-white rounded-xl px-2 py-6 my-6 w-full md:w-[500px] border shadow-xl shadow-black/30">
                      <div class="flex lg:flex-none lg:w-[120px] justify-center">
                        <img src="/prod-img/invertor-two.webp" class="w-[120px]"/>
                      </div>
                      <div class="flex-1">
                        <div class="flex flex-col gap-4 items-center justify-center">
                          <p class="text-gray-700 px-4 py-4 text-sm">Трансформаторные сварочные аппараты подойдут опытным пользователям «старой школы», которые планируют использовать сварку как для домашних, так и для рабочих нужд. Нестабильность электрической дуги делает этот вид аппарата сложным в эксплуатации для новичков.</p>
                          <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                            <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg px-12 py-2">
                              <nuxt-link :to="{ name: 'prods', query: { ct: 8 } }" class="text-white text-base">Перейти в каталог</nuxt-link>
                            </div>
                          </div>
                        
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="border-b border-gray-300 group">
                  <p class="text-sm cursor-pointer">Мастерам в автосервисах <span class="mdi mdi-help-circle-outline"></span></p>
                  <div class="absolute bottom-0 left-0 xl:left-auto transition invisible group-hover:visible opacity-0 group-hover:opacity-100 duration-500 ease-in-out group-hover:transform z-40 translate-y-0 group-hover:-translate-y-4">
                    <div class="grid grid-cols-1 md:flex items-center bg-white rounded-xl px-2 py-6 my-6 w-full md:w-[500px] border shadow-xl shadow-black/30">
                      <div class="flex lg:flex-none lg:w-[120px] justify-center">
                        <img src="/prod-img/semi-automatic.webp" class="w-[120px]"/>
                      </div>
                      <div class="flex-1">
                        <div class="flex flex-col gap-4 items-center justify-center">
                          <p class="text-gray-700 px-4 py-4 text-sm">Полуавтоматы рекомендуются для кузовных работ и восстановления алюминиевых запчастей.</p>
                          <div class=" text-sm text-gray-100 rounded-lg bg-blue-600 hover:bg-blue-700 border border-gray-300/50 dark:border-gray-500/50 transition-all duration-1000">
                            <div class=" bg-gradient-to-br from-gray-100/20 to-gray-900/40 rounded-lg px-12 py-2">
                              <nuxt-link :to="{ name: 'prods', query: { ct: 9 } }" class="text-white text-base">Перейти в каталог</nuxt-link>
                            </div>
                          </div>
                        
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>


          </div>


          <div class="my-10">
            <p class="text-xl">Тип сварки</p>
            <div class="my-2">
              <p class="">
                От этого параметра напрямую зависят сложность эксплуатации устройства, список рабочих металлов и качество полученного шва.
              </p>
              <p class="">
                В ручной дуговой <u><span style="font-size:18px"><em><strong>MMA-сварке</strong></em></span></u> применяются штучные электроды с обмазкой. Последняя при воздействии высоких температур формирует шлако-газовую защиту, которая затрудняет попадание кислорода в место контакта. Сварка этого типа позволяет использовать практически любые электроды, однако требует дополнительной обработки. Шлак следует очищать после каждого прохода, иначе качество шва существенно понижается.
              </p>
              <p class="">
                При покупке электродов обращайте внимание на тип — MMADC или MMAAC (для постоянного или переменного тока соответственно). Часто они не взаимозаменяемы. Для специфических материалов (чугун, медь, нержавейка) потребуются специализированные электроды.
              </p>
              <p class="">
                Сварка типа <u><span style="font-size:18px"><em><strong>MIG/MAG</strong></em></span></u> используется для сваривания цветных и черных металлов небольшой толщины. Для предотвращения окисления используется инертный (MIG) или активный (MAG) защитный газ. Идеально подойдет для тонких деталей, а также MIG/MAG единственный способ сварить материалы толщиной до одного миллиметра.
              </p>
              <p class="">
                <u><span style="font-size:18px"><em><strong>TIG</strong></em></span></u> — тип сварки тугоплавким электродом в среде инертного газа. Используется для цветных металлов, в том числе крупногабаритных деталей. Обычно применяется вольфрамовый электрод, у которого температура плавления доходит до 3500 градусов Цельсия.
              </p>
              <p>
                <u><span style="font-size:18px"><em><strong>Плазменная резка</strong></em></span></u> подойдет для нержавеющей и оцинкованной стали, алюминия, меди, латуни и других металлов. Рабочие температуры доходят до 30 тысяч градусов.
              </p>
            </div>
          

            <div class="bq-article md:mx-2 my-6 lg:mx-8">
              <p class="">
                Аппараты плазменной сварки схожи с инверторными, однако в горелке дополнительно присутствует специальный отсек для охлаждающей жидкости. Плазменная сварка требует опыта.
              </p>
            </div>
          </div>


          <div class="my-10">
            <p class="text-xl">Ключевые характеристики</p>
            <div class="my-2">
              <p class="my-4">
                <u><span style="font-size:18px"><em><strong>Входное напряжение</strong></em></span></u>. Его необходимо согласовать с имеющейся электросетью. Если часто возникают просадки или планируется регулярная работа от трансформатора с перепадами выходного напряжения, ищите сварочные аппараты с входным диапазоном 140–270 или 150–250 вольт (в зависимости от уровня просадок). Для работы в специфических условиях где сеть не дает даже 200 В стоит заказать сварочные аппараты с пониженным рабочим напряжением 150–160 В.
              </p>
              <p class="my-4">
                <u><span style="font-size:18px"><em><strong>Число фаз</strong></em></span></u>. Выпускаются модели для трехфазной и однофазной сети, а также комбинированные. Трехфазные сварочные устройства работают от сети 380 (реже 230) вольт. Они обеспечивают большую величину сварочного тока, поэтому способны сваривать толстостенные детали. Сфера применения: производство, строительные работы, кузни, СТО. Однофазные сварочные аппараты требуют сети 220 вольт, поэтому подойдут для бытового применения дома, в гараже или на даче. Если пользователь планирует использовать сварку не только для профессиональных целей, но и на дому, то стоит заказать модели с переключателем между одной и тремя фазами.
              </p>
              <p class="my-4">
                <u><span style="font-size:18px"><em><strong>Максимальный сварочный ток</strong></em></span></u>. Следует согласовывать с толщиной электродов. Чем выше сила сварочного тока, тем толще должен быть электрод. В свою очередь это позволяет работать с металлом большей толщины. Зависимость этих трех параметров приведена в следующей таблице:
              </p>

              <div class="flex justify-center">
                <table class="my-4 text-sm border-collapse hidden md:block">
                  <tbody>
                    <tr>
                      <td class=" border border-gray-300 dark:border-slate-700 px-2 py-2">Толщина металла, мм</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">1-3</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">3-4</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">4-5</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">5–6</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">6–8</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">8–11</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">11–15</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">15-18</td>
                    </tr>
                    <tr>
                      <td class=" border border-gray-300 dark:border-slate-700 px-2 py-2">Диаметр электрода, мм</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">1,0–1,5</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">1,6–2,0</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">2,0–2,4</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">2,5–3,1</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">3,2–3,9</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">4,0–4,9</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">5,0–5,9</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">От 6,0</td>
                    </tr>
                    <tr>
                      <td class=" border border-gray-300 dark:border-slate-700 px-2 py-2">Рекомендуемый сварочный ток, А</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">20–60</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">50–90</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">60–100</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">80–120</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">110–150</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">140–180</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">180–220</td>
                      <td class=" border border-gray-300 dark:border-slate-700 text-center px-4 py-2">220–260</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <p class="my-4 text-sm">
                Если вы не будете никогда работать с металлом толщиной в 10–15 миллиметров, то нет смысла покупать аппараты со сварочным током в 200 и более ампер.
              </p>
              <p class="my-4">
                <u><span style="font-size:18px"><em><strong>Напряжение холостого хода</strong></em></span></u> — разница в вольтах между анодом и катодом без дуги. Чем больше, тем проще создать электрическую дугу. Новичкам стоит выбирать модели с большим значением холостого хода, что существенно упрощает пуск. С другой стороны, высокое напряжение опасно для жизни человека, поэтому важно соблюдать требования безопасности.
              </p>
              <p class="my-4">
                <u><span style="font-size:18px"><em><strong>Рабочий цикл при максимальном сварочном токе</strong></em></span></u>. Измеряется в процентах. Например, число 30% показывает, что на максимальном сварочном токе техника способна работать 30% времени, а 70% будет остывать.
              </p>
              <p class="my-4">
                Если аппарат выдает сварочный ток до 150 ампер, то работать с деталями толщиной 6–8 миллиметров вы сможете только треть времени, после чего потребуется обязательное охлаждение.
              </p>
              <p class="my-4">
                Любительские модели мощностью до 2 кВт имеют показатель до 30%.
              </p>
              <p class="my-4">
                Для регулярной и продолжительной сварки понадобятся устройства от 4 кВт с рабочим циклом от 50%.
              </p>

            </div>
          </div>

          <p class="text-xl">Дополнительные опции</p>
          <div class="my-2">
            <p class="">
              Сварочные аппараты могут оснащаться функцией антиприлипания. Она распознает эффект прилипания и сбрасывает ток, что предотвращает приваривание электрода и необходимость его замены.
            </p>
            <p class="">
              Функция <u><span style="font-size:18px"><em><strong>горячего старта</strong></em></span></u> позволит работать с низкокачественными или поржавевшими электродами.
            </p>
            <p class="">
              Чтобы не допускать постоянного разрыва дуги, можно заказать модели с <u><span style="font-size:18px"><em><strong>форсажем</strong></em></span></u>. Опция повышает в нужный момент силу тока.
            </p>
            <p class="">
              Дополнительно сварочный аппарат может иметь <u><span style="font-size:18px"><em><strong>защиту от перегрузок</strong></em></span></u> и класс по IP, определяющий уровень влаго- и пыленепроницаемости.
            </p>
          </div>

        </div>



        
        <div class="my-4 md:my-8">
          <p class="text-xl my-4">Папулярные категории</p>
          <div v-if="true" class="flex items-center justify-start">
            <div id="" class="">
              <div class="flex flex-wrap gap-2 justify-start max-w-[800px]">
                <div v-for="(related, pk) in relateds" :key="pk" class="">
                  <div class="bg-white dark:bg-gray-800 rounded-xl border hover:border-gray-300 dark:border-gray-700 border-gray-200 hover:dark:border-gray-700 transition-all shadow-md">

                    <div class="flex items-center justify-center py-1 px-4">
                      <nuxt-link :to="{ name: 'prods', query: { ct: related.link }}" class="text-[10px] md:text-xs">{{ related.name }}</nuxt-link>
                    </div>

                  </div>
                </div>          
              </div>
            </div>
          </div>
        </div>






      </div>


    </div>

    <AppFooter />

  </div>
</template>