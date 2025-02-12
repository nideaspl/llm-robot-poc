## **运行步骤**
### **1. 启动 ROS 2**
确保 ROS 2 Humble 已安装，并启用了 `turtlesim`：
```bash
source /opt/ros/humble/setup.bash
```

### **2. 启动 `turtlesim`**
```bash
ros2 run turtlesim turtlesim_node
```

### **3. 运行 Python 代码**
```bash
python3 turtlesim_controller.py
```

### **4. 交互控制**
在终端输入：
```
Enter command (move forward, move backward, turn left, turn right, stop): move forward
```
然后 `turtlesim` 的小乌龟就会前进 🚀。

---

## **这个版本的优点**
✅ **超简单**：直接用 Python 字典替代 OpenAI API。  
✅ **无需 Flask**：通过 `input()` 在终端交互。  
✅ **直接控制 `turtlesim`**，无需额外转换。  
✅ **方便 POC 演示**：领导输入指令，马上看到效果。  

---
