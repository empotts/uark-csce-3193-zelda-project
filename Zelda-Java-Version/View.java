//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Assignment Description: This Assignment creates a map editor for our game. It uses keyboard inputs to move around the
//map and mouse inputs to place and remove tiles.
//View.java imports the Graphics class which handles much of the UI elements used in this project. 
//By using this, this class creates the window and environment used in this project.

import javax.swing.JPanel;
import java.awt.Graphics;

import java.awt.Color;



class View extends JPanel
{
	Model model;
	int viewX;
	int viewY;
	boolean editMode;
	boolean potMode;
	


	View(Controller c, Model m) //View Constructor
	{
		c.setView(this);
		model = m;
		viewX = 0; 
		viewY = 0;
		editMode = false;
		m.setView(this);
		
	}


	public void paintComponent(Graphics g)
	{
		
		g.setColor(new Color(128, 255, 255));
		g.fillRect(0, 0, this.getWidth(), this.getHeight());
		for(int i = 0; i < model.sprites.size(); i++)
		{
			model.sprites.get(i).draw(g,viewX,viewY);
			
		}
		
		if(editMode && !potMode)
		{
			g.setColor(Color.red);
			g.drawString("EDIT MODE", 600, 470);
		}
		if(editMode && potMode)
		{
			g.setColor(Color.red);
			g.drawString("POT MODE", 600, 470);
		}
		
	
		
	}
	//View Methods to change where the view window is repainted from
	public void moveUp()
	{
		if(viewY >= 500)
		{
			viewY -= 500;
		}
		return;
	}
	public void moveLeft()
	{
		if(viewX >= 700)
		{
			viewX -= 700;
		}
		return;
	}
	public void moveDown()
	{
		if(viewY <= 0)
		{
			viewY += 500;
		}
		return;
	}
	public void moveRight()
	{
		if(viewX <= 0)
		{
			viewX += 700;
		}
		return;
	}

	@Override
    public String toString()
    {
        return "";
    }
}

