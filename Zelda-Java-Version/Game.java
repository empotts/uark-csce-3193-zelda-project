//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Assignment Description: This Assignment creates a map editor for our game. It uses keyboard inputs to move around the
//map and mouse inputs to place and remove tiles.
//Game.java serves as the driver class for this project. It makes the necessary objects as attributes and runs the game as long as the window is open.

import javax.swing.JFrame;
import java.awt.Toolkit;

public class Game extends JFrame
{
	Model model;
	Controller controller;
	View view;

	public Game() //Game Constructor to initilize objects and create window
	{
		model = new Model();
		controller = new Controller(model);
		view = new View(controller,model);
		model.setView(view);
		this.setTitle("Zelda Game Java Version");
		this.setSize(700, 500);
		this.setFocusable(true);
		this.getContentPane().add(view);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		view.addMouseListener(controller);
		this.addKeyListener(controller);
		Json loadData = Json.load("map.json");
		model.unmarshal(loadData);
		System.out.println("Load Complete!");
		
		
	}


	public void run() //Runs game and update functions
	{
		while(true)
		{
			controller.update();
			model.update();
			view.repaint();  // This will indirectly call View.paintComponent
			Toolkit.getDefaultToolkit().sync(); // Updates screen

			// Go to sleep for 40 milliseconds
			try
			{
				Thread.sleep(40); //sleep for X ms, 1000/fps = delay
			} catch(Exception e) {
				e.printStackTrace();
				System.exit(1);
			}
			
			//System.out.println("hi"); // remove this line
		}
	}

	public static void main(String[] args) //Main
	{
		Game g = new Game();
		g.run();
	}

}
