import copy


def can_move_left(state):
	return not state[0][0]=='p'

def can_move_right(state):
	return not state[len(state)-1][0]=='p'

def cant_move(state):
	for i in range(len(state)):
		if state[i][0]=='p' and state[i][1]=='b':
			return 1
def can_eat(state):
	for i in range(len(state)):
		if state[i][0]=='p' and state[i][1]=='f':
			return 1

def move_left(state):
	if can_move_left(state):
		for i in range(len(state)):
			if state[i][0]=='p':
				state[i][0]=''
				state[i-1][0]='p'
				return state
			else:
				return state
def move_right(state):
	if cant_move(state):
		for i in range(len(state)): 
			if state[i][0]=='p' and state[i][1]=='b': 
				state[i][1]=''
				if can_move_right(state):
					for i in range(len(state)):
						if state[i][0]=='p':
							state[i][0]=''
							state[i+1][0]='p'
							return state
				else: 
					return state
					
	else:	
		if can_move_right(state):
			for i in range(len(state)):
				if state[i][0]=='p':
					state[i][0]=''
					state[i+1][0]='p'
					return state
		else:
			return state
#def unblock(state):
#	if cant_move(state):
#		for i in range(len(state)): 
#			if state[i][0]=='p' and state[i][1]=='b': 
#				state[i][1]=''
#				return state

def eat(state):
	if can_eat(state):
		for i in range(len(state)): 
			if state[i][0]=='p' and state[i][1]=='f': 
				state[i][1]=''
				return state

	else:
		return state

def find_children(state):
	children=[]
	
	
	#unblock_sate=copy.deepcopy(state)
	#child_unblock=unblock(unblock_state)
	right_state=copy.deepcopy(state)
	child_right=move_right(right_state) 
	left_state=copy.deepcopy(state)
	child_left=move_left(left_state) 
	eat_state=copy.deepcopy(state)
	child_eat=eat(eat_state) 
	
	
	#if not child_unblock==state:
		#children.append(child_unblock)
	if not child_eat==state:
		children.append(child_eat)
	if not child_left==state: 
		children.append(child_left) 
	if not child_right==state:
		children.append(child_right) 
	return children 



def make_front(state):
    return [state]



def expand_front(front, method):  
    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)
    
    #elif method=='BFS':
    #elif method=='BestFS':
    #else: "other methods to be added"        
    
    return front



def make_queue(state):
    return [[state]]



def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)
    
    #elif method=='BFS':
    #elif method=='BestFS':
    #else: "other methods to be added" 
    
    return queue_copy
            



def find_solution(front, queue, closed, goal, method):
       
    if not front:
        print('_NO_SOLUTION_FOUND')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)
    
    #elif is_goal_state(front[0]):
    elif front[0]==goal:
        print('_GOAL_FOUND_')
        print(queue[0])
    
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)
        
        

          
def main():
    
    initial_state=[['',''],['p','f'],['','b'],['','f'],['','b'],['','f']]
    goal=[['',''],['',''],['',''],['',''],['',''],['p','']]
    method='DFS'
    	
    
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], goal, method)
        

if __name__ == "__main__":
    main()
