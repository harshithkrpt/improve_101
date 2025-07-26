#!/usr/bin/env bash

### CONFIGURE THESE ###
SESSION="dev"
PROJECT_DIR="/home/harshith/Downloads/improve_101/interview_readyness/system-design/interview_ready_system_design_simplified/3.high_level_design/1.mail_system_design/gmail-clone"
### END CONFIGURATION ###

# Start session (detached) with initial window named 'dev'
tmux new-session -d -s "$SESSION" -c "$PROJECT_DIR" -n dev

# Pane 0 (top-left): coding
tmux send-keys -t "$SESSION":0.0 "cd $PROJECT_DIR" C-m

# Split pane 0 vertically → pane 1 (top-right)
tmux split-window -h -t "$SESSION":0.0 -c "$PROJECT_DIR"
# In pane 1, show memory usage every 2 seconds
tmux send-keys -t "$SESSION":0.1 "watch -n2 free -h" C-m

# Back to pane 0, split it horizontally → pane 2 (bottom-left)
tmux select-pane -t "$SESSION":0.0
tmux split-window -v -t "$SESSION":0.0 -c "$PROJECT_DIR"
# In pane 2, tail your Docker Compose logs
tmux send-keys -t "$SESSION":0.2 "cd $PROJECT_DIR && docker-compose logs -f" C-m

# Finally, split pane 1 horizontally → pane 3 (bottom-right)
tmux select-pane -t "$SESSION":0.1
tmux split-window -v -t "$SESSION":0.1 -c "$PROJECT_DIR"
# Pane 3 is left ready for misc commands
tmux send-keys -t "$SESSION":0.3 "cd $PROJECT_DIR" C-m

# Select pane 0 (coding) on attach
tmux select-pane -t "$SESSION":0.0

# Attach to the session
tmux attach -t "$SESSION"

