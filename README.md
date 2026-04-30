# zhtc
# 数据驱动的短时停车需求预测与动态引导系统
本仓库是一套完整的**数据驱动的短时停车需求预测与动态引导系统**工程，涵盖前端、后端、数据库初始化全链路代码与配置，旨在实现停车需求的智能预测、停车资源的动态引导与管理。

## 一、项目概述
系统聚焦城市短时停车需求场景，基于数据驱动的算法模型实现停车需求预测，并通过前端可视化、后端业务逻辑支撑，完成停车资源的动态引导与用户管理，核心解决“停车难、资源分配不均”问题。
仓库包含两套工程环境（`zhtc`/`gxdc`前缀），适配不同业务场景/部署环境的诉求，整体具备完整的用户身份管理、停车需求预测、资源引导调度能力。

## 二、技术栈
### 后端
- 开发语言：Java
- 构建工具：Maven（含`mvnw`/`mvnw.cmd`跨平台构建脚本）
- 核心能力：业务逻辑处理、停车预测算法对接、数据库交互、接口提供

### 前端
- 包管理：npm（通过`package-lock.json`固化依赖版本）
- 核心模块：用户登录、身份管理、停车数据可视化、引导指令展示

### 数据层
- 脚本类型：SQL（数据库初始化）
- 作用：创建业务表、初始化基础配置数据

## 三、目录结构说明
| 目录/文件                | 类型       | 核心说明                                                                 |
|--------------------------|------------|--------------------------------------------------------------------------|
| `README.md`              | 文档       | 项目总览、使用说明                                                       |
| `package-lock.json`      | 配置文件   | 前端npm依赖版本锁文件，保障多环境依赖一致性                             |
| `zhtc-front/`            | 前端工程   | 主业务线前端代码，含`Login/`（登录模块）、`User/`（用户模块）等核心模块  |
| `gxdc-front/`            | 前端工程   | 备用/测试环境前端代码，模块结构与`zhtc-front`一致                       |
| `sql/init_db.sql`        | 数据库脚本 | 数据库初始化脚本，创建业务表、初始化基础数据（如用户角色、停车区域配置） |
| `zhtc-master/`           | 后端工程   | 主业务线后端代码，Maven工程，含核心业务逻辑、接口、算法对接逻辑          |
| `gxdc-master/`           | 后端工程   | 备用/测试环境后端代码，工程结构与`zhtc-master`一致                       |
| `.gitignore`             | 配置文件   | Git版本控制忽略规则，屏蔽编译产物、日志、依赖包等无需提交的文件          |

## 四、环境准备
### 基础依赖
1. 后端：JDK 8+、Maven 3.6+（或直接使用工程内`mvnw`/`mvnw.cmd`）
2. 前端：Node.js 14+、npm 6+
3. 数据库：MySQL 5.7+/PostgreSQL 12+（适配`init_db.sql`语法）
4. 运行环境：Linux/Windows/macOS（跨平台兼容）

## 五、快速启动
# 数据驱动的短时停车需求预测与动态引导系统 - 安装说明
本文档详细说明本系统的完整安装部署流程，涵盖**数据库、后端、前端**全环节，适配 Windows/Linux/macOS 主流操作系统，适用于开发/测试/演示环境部署。

## 一、适用范围
本安装说明针对仓库内 `zhtc` 主业务线工程（`gxdc` 备用/测试工程部署流程完全一致，仅需替换目录名），完成部署后可实现系统全功能运行。

## 二、环境准备
### 1. 硬件要求（最低配置）
- CPU：双核 2.0GHz 及以上
- 内存：4GB 及以上
- 硬盘：20GB 可用空间（含依赖、编译产物、数据库存储）

### 2. 软件依赖（必须安装）
| 组件         | 版本要求       | 作用                     | 下载地址（官方）                                                                 |
|--------------|----------------|--------------------------|----------------------------------------------------------------------------------|
| JDK          | 8 及以上       | 后端 Java 程序运行/编译  | [Oracle JDK](https://www.oracle.com/cn/java/technologies/downloads/)、[OpenJDK](https://openjdk.org/install/) |
| Node.js      | 14.x 及以上    | 前端依赖安装/运行        | [Node.js 官网](https://nodejs.org/zh-cn/download/)                                |
| MySQL        | 5.7+/8.0+      | 数据库服务（核心存储）   | [MySQL 官网](https://dev.mysql.com/downloads/mysql/)                              |
| Maven        | 3.6+（可选）| 后端编译构建（也可使用工程内 `mvnw` 脚本） | [Maven 官网](https://maven.apache.org/download.cgi)                               |

### 3. 环境验证（安装后确认）
打开终端/命令提示符，执行以下命令验证依赖是否安装成功：
```bash
# 验证 JDK
java -version  # 输出 JDK 版本号（如 1.8.0_301）

# 验证 Node.js & npm
node -v        # 输出 Node 版本号（如 v14.17.0）
npm -v         # 输出 npm 版本号（如 6.14.13）

# 验证 MySQL
mysql -V       # 输出 MySQL 版本号（如 mysql  Ver 8.0.28 for Win64 on x86_64）

# 验证 Maven（若手动安装）
mvn -v         # 输出 Maven 版本号（如 Apache Maven 3.8.5）
```

## 三、详细安装步骤
###  1：数据库部署（核心前置）
#### 1.1 启动 MySQL 服务
- **Windows**：打开“服务”面板，找到 `MySQL` 服务并启动（或执行 `net start mysql`）；
- **Linux/macOS**：执行 `systemctl start mysqld`（CentOS）/ `brew services start mysql`（macOS）。

#### 1.2 创建数据库
登录 MySQL 控制台，创建系统专用数据库（示例名：`parking_system`）：
```bash
# 登录 MySQL（默认账号 root，按提示输入密码）
mysql -u root -p

# 创建数据库（字符集适配中文，避免乱码）
CREATE DATABASE parking_system DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

# 退出控制台
exit;
```

#### 1.3 执行初始化脚本
将仓库内 `sql/init_db.sql` 脚本导入新建的数据库：
```bash
# 执行脚本（替换 [你的密码] 为 MySQL root 密码，Windows/Linux 通用）
mysql -u root -p[你的密码] parking_system < sql/init_db.sql

# 示例（密码为 123456）：
# mysql -u root -p123456 parking_system < sql/init_db.sql
```
> 验证：登录 MySQL，执行 `USE parking_system; SHOW TABLES;`，若能看到多张业务表（如 user、parking_area 等），说明脚本执行成功。

###  2：后端工程部署（zhtc-master）
#### 2.1 配置数据库连接
进入后端工程目录，修改数据库配置文件（适配本地 MySQL 地址/账号/密码）：
```bash
# 进入后端工程目录
cd zhtc-master/src/main/resources/
```
找到配置文件（如 `application.yml`/`application.properties`），修改数据库连接参数：
```yaml
# 示例（application.yml）
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/parking_system?useUnicode=true&characterEncoding=utf8mb4&useSSL=false&serverTimezone=Asia/Shanghai
    username: root  # 替换为你的 MySQL 账号
    password: 123456  # 替换为你的 MySQL 密码
    driver-class-name: com.mysql.cj.jdbc.Driver
```

#### 2.2 编译 & 启动后端服务
回到后端工程根目录（`zhtc-master/`），执行启动命令：
| 操作系统       | 启动命令                                                                 |
|----------------|--------------------------------------------------------------------------|
| Linux/macOS    | `./mvnw spring-boot:run`（无需手动安装 Maven，使用工程内置脚本）|
| Windows        | `mvnw.cmd spring-boot:run`                                               |
| 手动安装 Maven | `mvn spring-boot:run`（全系统通用）|

> 启动成功标志：终端无报错，最后输出 `Started ZhtcApplication in XX seconds (JVM running for XX)`。

### 3.前端工程部署（zhtc-front）
#### 3.1 安装前端依赖
进入前端工程目录，执行 npm 安装依赖：
```bash
# 进入前端工程目录
cd zhtc-front

# 安装依赖（使用 package-lock.json 固化版本，避免依赖冲突）
npm install
```
> 若安装缓慢，可切换国内镜像：`npm install --registry=https://registry.npm.taobao.org`。

#### 3.2 配置后端接口地址（可选）
若后端服务端口/地址非默认（默认 `http://localhost:8080`），需修改前端接口配置文件（如 `src/config/api.js`/`src/utils/request.js`）：
```javascript
// 示例（request.js）
const baseURL = 'http://localhost:8080'; // 替换为实际后端地址+端口
```

#### 3.3 启动前端服务
在前端工程目录执行启动命令：
```bash
# 启动本地开发服务（默认端口 8081，可在 vue.config.js/react.config.js 中修改）
npm run serve

# 若为生产打包部署（可选）：
# npm run build  # 编译产物输出到 dist 目录，可部署到 Nginx/Apache
```
> 启动成功标志：终端输出 `App running at:  - Local:   http://localhost:8081/`。

## 4、启动验证
完成以上步骤后，验证系统是否正常运行：
1. 打开浏览器，访问 `http://localhost:8081`（前端地址）；
2. 页面显示系统登录界面，输入初始化账号（默认账号/密码可在 `init_db.sql` 中查看，如 `admin/123456`）；
3. 登录成功后，可查看“停车需求预测”“资源引导”等核心模块，说明系统部署完成。

## 5、常见问题排查
| 问题现象                  | 排查方向                                                                 |
|---------------------------|--------------------------------------------------------------------------|
| 后端启动报错“数据库连接失败” | 1. 检查 MySQL 服务是否启动；2. 核对配置文件中数据库地址/账号/密码；3. 确认 parking_system 数据库已创建 |
| 前端启动后无法访问后端接口 | 1. 检查后端服务是否正常启动；2. 核对前端接口配置的地址/端口；3. 关闭本地防火墙（开发环境）|
| npm install 安装失败       | 1. 检查 Node.js 版本是否≥14；2. 清理 npm 缓存（`npm cache clean --force`）；3. 切换国内镜像 |
| 前端页面空白/报错         | 1. 检查浏览器控制台报错信息；2. 确认依赖安装完整（无 npm install 报错）；3. 核对前端配置文件 |

## 6、注意事项
1. **多环境切换**：若需部署 `gxdc` 工程，仅需将上述步骤中的 `zhtc-master`/`zhtc-front` 替换为 `gxdc-master`/`gxdc-front`，流程完全一致；
2. **端口冲突**：若 8080（后端）/8081（前端）端口被占用，可修改后端 `application.yml` 中的 `server.port`、前端 `vue.config.js` 中的 `devServer.port`；
3. **生产环境建议**：
   - 后端：使用 `nohup java -jar target/zhtc-master-0.0.1-SNAPSHOT.jar &` 后台运行；
   - 前端：将 `npm run build` 编译后的 `dist` 目录部署到 Nginx，并配置反向代理指向后端接口；
   - 数据库：开启定时备份，避免数据丢失。
4. **依赖版本兼容**：禁止随意降级 JDK/Node.js 版本，否则可能导致工程编译/运行失败。

## 六、核心功能模块
1. **用户管理模块**：登录认证、身份权限控制、用户信息维护；
2. **停车需求预测模块**：对接数据驱动算法，实现短时（分钟/小时级）停车需求预测；
3. **动态引导模块**：基于预测结果，展示停车资源分布、推荐最优停车区域；
4. **数据可视化模块**：停车需求趋势、资源利用率、引导效果等数据图表展示；
5. **系统配置模块**：停车区域、预测算法参数、引导规则等基础配置管理。

## 七、注意事项
1. 两套工程（`zhtc`/`gxdc`）启动逻辑一致，可根据部署环境选择对应工程；
2. 前端`package-lock.json`需与`npm install`配合使用，避免依赖版本不一致；
3. 数据库脚本执行前需确认数据库版本兼容性，若使用非MySQL数据库，需微调`init_db.sql`语法；
4. 后端启动前需确保数据库服务正常，且配置文件中数据库连接信息正确。

## 八、维护说明
- 前端依赖更新：执行`npm update`并更新`package-lock.json`；
- 后端依赖更新：修改`pom.xml`后执行`mvn clean install`；
- 数据库结构调整：更新`sql/init_db.sql`并重新执行初始化（生产环境需注意数据备份）。
