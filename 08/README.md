### Профилирование с помощью декоратора @profile
#### Профилирование создания классов

![profile_create](https://github.com/EvdokimovaA/deep_python_23_EvdokimovaA/blob/master/08/profile_create.PNG)

Больше всего памяти занимают экземпляры класса WeakClass, меньше всего - класса SlotsClass.

#### Профилирование изменения классов

![profile_change](https://github.com/EvdokimovaA/deep_python_23_EvdokimovaA/blob/master/08/profile_change.PNG)

Изменение атрибутов у всех классов занимает примерно один и тот же объём памяти 

### Профилирование с помощью cProfile

![profile_time](https://github.com/EvdokimovaA/deep_python_23_EvdokimovaA/blob/master/08/profile_time.PNG)

***Профилирование по памяти и по времени проводилось раздельно, совместные результаты можно увидеть в файле [all_results](https://github.com/EvdokimovaA/deep_python_23_EvdokimovaA/blob/master/08/all_results.txt)***

### Замеры времени создания и изменения экземпляров классов через time

![time](https://github.com/EvdokimovaA/deep_python_23_EvdokimovaA/blob/master/08/time.PNG)

Из скриншота видно, что дольше всех создаются экземпляры класса со слотами, но изменяются они быстрее, чем экземпляры обычного класса. 
Экземпляры обычного класса создаются быстрее всех, но меняются дольше всех. Экземпляры класса с weakref меняются быстрее всех, 
но создаются дольше, чем экземпляры обычного класса.