
# Project Testing

## Navigation Testing

shell 1: (environment gazebo rviz move_base slam gmapping)

```
roslaunch erl_assignment_3_robot detectibot_environment.launch
```

shell 2: (navigation node)

```
rosrun erl_assignment_3 navigation.py
```

## Vision Testing

shell 1:


```
roslaunch erl_assignment_3_robot detectibot_environment.launch
```

shell 2:

```
rosrun erl_assignment_3 img_echo
```

shell 3:

```
rosrun erl_assignment_3 detectibot_magnifier
```

## State machine test

shell 1:

```
roslaunch erl_assignment_3_robot detectibot_environment.launch
```

shell 2:

```
rosrun erl_assignment_3 img_echo &
rosrun erl_assignment_3 detectibot_magnifier &
rosrun erl_assignment_3 navigation.py 
```

shell 3:

```
rosrun erl_assignment_3 cluedo_kb.py
```

shell 4:

```
rosrun erl_assignment_3 state_machine.py
```
