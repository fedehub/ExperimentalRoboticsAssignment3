<div id="top"></div>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]





<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/fedehub/expTest">
    <img src="media/miscellaneous/logo-black.png" alt="Logo" width="200" height="100">
  </a>

  <h3 align="center">Experimental Robotics Laboratory</h3>

  <p align="center">
    First assignment for the Experimental Robotics laboratory course 
    <br />
    <a href="https://github.com/fedehub/expTest/doc"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/fedehub/expTest/demo">View Demo</a>
    ·
    <a href="https://github.com/fedehub/expTest/issues">Report Bug</a>
    ·
    <a href="https://github.com/fedehub/expTest/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#software architechture">Software architechture</a></li>
        <li><a href="#ROS node description">ROS node description</a></li>
          <ul>
            <li><a href=#rossrv>rossrv</a></li>
            <li><a href=#rosmsg>rosmsg</a></li>
            <li><a href=#rostopic>rostopic</a></li>
            <li><a href=#rosparam>rosparam</a></li>
          </ul>
        <li><a href="#rqt_graph">rqt_graph</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running procedure">Running procedure</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#Working hypothesis and environment">Working hypothesis and environment</a>
      <ul>
        <li><a href="#System's features">System's features</a></li>
        <li><a href="#System's limitations">System's limitations</a></li>
        <li><a href="#Possible technical Improvements">Possible technical Improvements</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- PLEASE INSERT HERE -->


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

<!-- PLEASE INSERT HERE -->


* [Smach][1]
* [Armor][2]
* [ROS][4]


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Under the following sections, the software architecture is briefly introduced, along with the prerequisites and installation procedures. Then, a quick video demonstration showing the overall functioning is provided and system’s limitations are discussed

### Software architechture

<!-- how to make a ref to a specific section 
the **rqt_graph** <a href="#rqt_graph">section</a>
-->
 Please consider that **consistent hypothesis** have been defined as COMPLETED but NOT INCONSISTENT 

> *REMARK* A consistent hypothesis is  defined as *completed* when there occurs one role for each class (i.e., one occourence of what, one occourence for who, one occourence for where ). 
A straightforward example of such hypothesis is [ID2][12], whose definition is here below reported

```
ID2_1: ['where', 'Study']
ID2_2: ['who', 'Col.Mustard']
ID2_3: ['what', 'Rope']
```

> *REMARK* An hypothesis, is defined as *inconsistent* when there occurs more than one role for each class (i.e. 2 or more occourences of who, where, what) 

A clear example of such hypothesis is [ID4][12], whose definition is here below reported

```
ID4_1: ['where', 'Library']
ID4_2: ['who', 'Mrs.White']
ID4_3: ['what', 'LeadPipe']
ID4_4: ['where', 'Diningoom']
```
<!-- PLEASE INSERT HERE -->



<!-- Software architecture, temporal diagram and states diagrams (if applicable). Each diagram should be commented with a paragraph, plus a list describing ROS messages and parameters. -->

### ROS node description

Within the scripts folder, the following nodes are listed:  
- [Nodo1.py][5]:              <!-- PLEASE INSERT HERE -->

- [robotcontroller.py][6]:    <!-- PLEASE INSERT HERE -->

  
- [navigation.py][7]:         <!-- PLEASE INSERT HERE -->


- [oracle.py][8]:             <!-- PLEASE INSERT HERE -->


### rossrv 

- **query_oracle**: <!-- PLEASE INSERT HERE -->

    
  > msg type:       <!-- PLEASE INSERT HERE -->

  
- **ask_for_hint**: <!-- PLEASE INSERT HERE -->

  > msg type:       <!-- PLEASE INSERT HERE -->


- **detectiBotSwitch**:     <!-- PLEASE INSERT HERE -->

  > msg type                <!-- PLEASE INSERT HERE -->


### rosmsg

<!-- PLEASE INSERT HERE -->


### rostopic

The aforementioned message type use the `/robotPose` topic. It presents as:
- **Publishers:**
  - [/navigation][7]
  - [/controller][6] 
- **Subscribers:**
  - [/navigation][7]



### rosparameters 

<!-- PLEASE INSERT HERE -->


### rqt_graph
The *rqt_graph* is a tool that shows the correlation among active nodes and messages being transmitted on the ROS network as a diagram. After executing all nodes (or after launching the roslaunch file), launch the **rqt_graph** through 

```
rosrun rqt_graph rqt_graph
```

In the figure below, circles represent nodes and squares represent topic messages. The arrow instead, indicates the transmission of the message!

<!-- PLEASE INSERT HERE -->


### Installation procedure

## The fastest way

1. Clone the repo

```sh
   git clone https://github.com/fedehub/ExperimentalRoboticsAssignment3.git
```
2. Move to the directory and enable permissions

```sh
   cd <!-- PLEASE INSERT HERE -->

   chmod +x "./compile,sh
```
3. launch the `compile.sh` file

```sh
   <!-- PLEASE INSERT HERE -->

```
4. launch the project simulation

```sh
   <!-- PLEASE INSERT HERE -->

```

5. pub a message from terminal, when prompted

```python
<!-- PLEASE INSERT HERE -->

```
## step by step 


- type here ...

```sh
docker pull carms84/exproblab
```

- type here ...

```sh
docker run -it --name exprob -p 6080:80 -p 5900:5900 carms84/exproblab
```

- type here ...

```sh
cd ros_ws/src 
```

- type here ...

```sh
git clone https://github.com/fedehub/ExperimentalRoboticsAssignment3.git
```

- type here ...

```sh

```

- type here ...
 
```sh

```

- type here ...

```sh

```
- type here ...

```sh

```

- type here ...

```sh

```

### further changes ...

<!-- PLEASE INSERT HERE -->

                  

## Workspace building e launch

- type here ...

```sh
cd /home/ros_ws/
catkin_make
```

- type here ...

```python


```

- type here ...

```python

```

<p align="right">(<a href="#top">back to top</a>)</p>

### Running procedure
<!-- including all the steps to display the robot's behavior -->
To appreciate the robot's behaviour, first of all:

```sh
roslaunch ...

```
Alternatively, it is also possible to launch each node, sequentially, after having started the `roscore`:


```sh
roscore &

```

type here ...

```sh


```

Then,

```sh
rosrun expTest oracle.py

```
It follows,

```sh
rosrun expTest navigation.py

```

then, 


```sh
rosrun expTest detectiBot.py

```

and finally,

```sh
rosrun expTest robotController.py

```

By starting the smach_viewer node


```sh
rosrun smach_viewer smach_viewer.py

```

it is possible to see how the logic is implemented and how the transitions take place



<!-- USAGE EXAMPLES -->
## Usage

The most relevant aspects of the project and a brief video tutorial on how to launch the simulation can be found [here][105]

<!-- A commented small video, a GIF or screenshots showing the relevant parts of the running code. -->





<p align="right">(<a href="#top">back to top</a>)</p>

## Working hypothesis and environment 

The  architecture  is designed for providing a raw simplification of the Cluedo Game. Hints are set a-priori, as well as true hypothesis that leads to the game’s end, once collected. 

All choices were made with the aim of making the system as modular and flexible as possible. Despite this, certain limitations make the system quite unrealistic but functional.

### System's features

Most of them have been already discussed in the Software architecture’s section. The most relevant one is that of having a robot capable of exploiting an ontology to solve  a problem.

### System's limitations

type here ...

### Possible technical Improvements

type here ...

<!-- ROADMAP -->
## Roadmap

- [x] Complete the introduction of the template 
- [ ] Describe the software architechture
  - [ ] Component diagram (*not mandatory*)
  - [ ] Temporal diagram + comments
  - [ ] States diagrams, whether applicable + comments
  - [ ] Create a list describing ROS messages and parameters 
- [ ] Describe the installation steps and the running procedures
    - [ ] Create a dedicated paragraph
    - [ ] Include all the steps to display the robot's behaviour
- [ ] Show in the "usage" section the running code
  - [ ] Create a small video tutorial of the launch
  - [ ] Create a small animated gif of the terminal while running code
- [ ] Describe the Working hypothesis and environment
  - [ ] Dedicated section for System's features
  - [ ] Dedicated section for System's limitations
  - [ ] Dedicated section for Possible technical improvements

 
 
    

See the [open issues](https://github.com/fedehub/expTest/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement"

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under none License. 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Federico Civetta - s4194543@studenti.unige.it

Project Link: [https://github.com/fedehub/expTest](https://github.com/fedehub/expTest)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## List of resources

* [Viewing state machine](http://wiki.ros.org/smach/Tutorials/Smach%20Viewer)
* [Smach](http://wiki.ros.org/smach)
* [Armor](https://github.com/EmaroLab/armor)
* [Protègè](https://protege.stanford.edu)




<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[forks-shield]: 	https://img.shields.io/github/forks/fedehub/ExperimentalRoboticsAssignment3
[forks-url]: https://github.com/fedehub/ExperimentalRoboticsAssignment3/network/members
[stars-shield]: 	https://img.shields.io/github/stars/fedehub/ExperimentalRoboticsAssignment3
[stars-url]: https://github.com/fedehub/ExperimentalRoboticsAssignment3/stargazers
[issues-shield]: 	https://img.shields.io/github/issues/fedehub/ExperimentalRoboticsAssignment3
[issues-url]: https://github.com/fedehub/expTest/issues
[license-shield]: https://img.shields.io/github/license/fedehub/ExperimentalRoboticsAssignment3


[1]: http://wiki.ros.org/smach
[2]: https://github.com/EmaroLab/armor
[3]: http://wiki.ros.org/smach/Tutorials/Smach%20Viewer
[4]: http://wiki.ros.org
[5]: <sherlbotH_holes.py>
[6]: <robotcontrolelr>
[7]: <navigation>
[8]: <oracle>
[9]: <HypoID_Msg>
[10]: <Hint_Msg>
[11]: <BotMsg_Msg>
[12]: <param.yaml file>
[13]: <msgFolder>
[14]: <robotPose.msg>
[15]: armor_manipulation_client.py
[16]: https://ontogenesis.knowledgeblog.org/1260/
[17]: http://emarolab.github.io/armor_py_api/armor_utils_client.html
[18]: https://docs.python.org/3/library/queue.html
[19]: https://protege.stanford.edu

[100]: https://github.com/fedehub/expTest/blob/main/media/componentDiagram/componentDiagram.jpg
[101]: https://github.com/fedehub/expTest/blob/main/media/rqt/rosgraph.svg
[102]: https://github.com/fedehub/expTest/blob/main/media/sequenceDiagram/sequenceDiagram.jpg
[103]: https://github.com/fedehub/expTest/blob/main/media/stateDiagram/stateDiagram.jpg
[104]: https://github.com/fedehub/expTest/blob/main/media/entity_graph.jpg
[105]: <youTubeVideo>
[106]: https://github.com/fedehub/expTest/blob/main/media/gifs/smach.gif
