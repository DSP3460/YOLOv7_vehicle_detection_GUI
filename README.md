# YOLOv7_vehicle_detection_GUI
基于改进YOLOv7算法的车辆目标检测系统。
1、实现FPS获取 YoloClass第127行
2、实现slider和spin互相转化  recognition第34行
3、对文件窗口说明进行了优化  recognition第174行
4、对pt模型文件存放位置进行了变更
5、调整了检测框线宽 YoloClass第180行


** 2.19
common.py yolo.py模块均进行了变更 适配检测KITTI三类（car、cyclist、perdstrian）数据模型


** 2.29

**！！！当更换图片素材，需要重新配置qrc资源路径名称
**！！！同时利用《资源文件配置说明》第2、3步重新生成apprcc.py，导入可省略

apprcc.qrc是一个XML格式的文件，根节点为RCC，里面包含若干qresource节点，
每个qresource有自己的 prefix(路径前缀)属性,qresource节点包含了若干file节点，
描述了各个文件相对于.qrc的路径。

《资源文件配置说明》
1、创建qrc文件，配置资源路径
2、使用pyside2-rcc -o apprcc_rc.py  apprcc.qrc将qrc转为py
3、加载ui时，将apprcc_rc.py改为apprcc.py，同时导入apprcc.py
4、在代码中引用资源中的文件时，路径为：********冒号+prefix路径前缀+file相对路径**************


目录结构
---img
    ---icons
    ---example.png
---ui
    ---main.ui
---apprcc.qrc
---apprcc_rc.py


菜单栏Tools/External Tools中
Pyside6_Designer：用于快速设计、修改 ui 并生成 .ui 文件。
Pyside6_UIC：将制作好的 .ui 文件转化为 .py 文件
Pyside6_RCC：将资源文件 .rcc 文件转换成 .py文件

