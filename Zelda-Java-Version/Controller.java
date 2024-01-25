//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Assignment Description: This Assignment creates a map editor for our game. It uses keyboard inputs to move around the
//map and mouse inputs to place and remove tiles.
//Controller.java handles the user inputs and sends updates to the view and model objects.

import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;

class Controller implements ActionListener, MouseListener, KeyListener
{
	View view;
	Model model;
	boolean keyLeft;
	boolean keyRight;
	boolean keyUp;
	boolean keyDown;
	
	
	Controller(Model m) //Constructor, class handels all user inputs
	{
		model = m;
		
				
	}

	public void actionPerformed(ActionEvent e)
	{
		
	}

	public void setView(View v)
	{
		view = v;
	}


	//Mouse Methods
	
	public void mousePressed(MouseEvent e) //mouse presses handled
	{
		if(view.editMode && !view.potMode)
		{
			model.placeTile(e.getX()+view.viewX, e.getY()+view.viewY);
		}
		if(view.editMode && view.potMode)
		{
			model.placePot(e.getX()+view.viewX, e.getY()+view.viewY);
		}
	}

	public void mouseReleased(MouseEvent e) {    }
	public void mouseEntered(MouseEvent e) {    }
	public void mouseExited(MouseEvent e) {    }
	public void mouseClicked(MouseEvent e) {    }

	//Keyboard Methods

	public void keyPressed(KeyEvent e) //key strokes handles
	{
		switch(e.getKeyCode())
		{
			case KeyEvent.VK_RIGHT: 	keyRight = true; 	break; // Unused for now
			case KeyEvent.VK_LEFT: 		keyLeft = true; 	break;
			case KeyEvent.VK_UP: 		keyUp = true; 		break;
			case KeyEvent.VK_DOWN: 		keyDown = true; 	break;
			case KeyEvent.VK_Q: 		System.exit(0); 	break; //Exits game if Q key or ESC key are pressed
			case KeyEvent.VK_ESCAPE: 	System.exit(0); 	break;
			case KeyEvent.VK_W: 		if(view.editMode){view.moveUp();}		break; //Calls methods to shift the screen when WAXD are pressed
			case KeyEvent.VK_A: 		if(view.editMode){view.moveLeft(); }	break;
			case KeyEvent.VK_X: 		if(view.editMode){view.moveDown(); }	break;
			case KeyEvent.VK_D: 		if(view.editMode){view.moveRight(); }	break;
			
			
		}
	}

	public void keyReleased(KeyEvent e)
	{
		switch(e.getKeyCode())
		{
			case KeyEvent.VK_RIGHT: 	keyRight = false;		break; // Unused for now
			case KeyEvent.VK_LEFT: 		keyLeft = false; 		break;
			case KeyEvent.VK_UP: 		keyUp = false; 			break;
			case KeyEvent.VK_DOWN: 		keyDown = false; 		break;
			case KeyEvent.VK_CONTROL: 	model.sendBoomerang();	break;
		}
		char c = Character.toLowerCase(e.getKeyChar());
		switch(c)
		{
			case 's': // Saves data
			{
				Json saveData = model.marshal();
				saveData.save("map.json");
				System.out.println("Save Complete!");
				break;

			}
			case 'l': //Loads data
			{
				Json loadData = Json.load("map.json");
				model.unmarshal(loadData);
				System.out.println("Load Complete!");
				break;
			}
			case 'e':
			{
				view.editMode = !view.editMode;
				break;
			}
			case 'p':
			{
				view.potMode = !view.potMode;
			}
		}

	}

	public void keyTyped(KeyEvent e)
	{
		
	}

	void update() // unused for now
	{
		if(keyRight) 	{model.link.x+=10; model.link.cycleRight();}
		if(keyLeft) 	{model.link.x-=10; model.link.cycleLeft();}
		if(keyDown) 	{model.link.y+=10; if(!keyRight && !keyLeft) model.link.cycleDown();}
		if(keyUp) 		{model.link.y-=10; if(!keyRight && !keyLeft) model.link.cycleUp();}


		if(model.link.x+model.link.w/2>700)
		{
			view.moveRight();
		}
		if(model.link.x+model.link.w/2<700)
		{
			view.moveLeft();
		}
		if(model.link.y+model.link.h/2>500)
		{
			view.moveDown();
		}
		if(model.link.y+model.link.h/2<500)
		{
			view.moveUp();
		}
		
	}

	

}
