//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Link.java established the image and functions of the link character in the game.

import java.awt.Graphics;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;



public class Link extends Sprite
{
   
    int speed;
    int prevX;
    int prevY;
    static BufferedImage[] linkImages = null;
	static int numLinkImages;
	int currentLinkImage;
	int direction; 	//0 = down, 1 = left, 2 = up, 3 = right

	


    public Link(int x, int y)
    {
       	super(x,y);
		prevX = x;
		prevY = y;
        numLinkImages = 50;
		currentLinkImage = 0;
		speed = 0;
		w = 50;
		h = 50;
        
		setTag("LINK");
		if(linkImages == null)
		{
			linkImages = new BufferedImage[numLinkImages];
			try //Imports png images
			{
				linkImages = new BufferedImage[numLinkImages];

				for(int i = 0; i < numLinkImages; i++)
				{
					String pathName = "ImageFolder/link";
					if(i<9)
					{
						pathName = pathName + "0" + Integer.toString(i+1) + ".png";
						//System.out.println(pathName);
					}
					else
					{
						pathName = pathName + Integer.toString(i+1) + ".png";
						//System.out.println(pathName);
					}
					linkImages[i] = ImageIO.read(new File(pathName));
				}
				//System.out.println(x + "," + y); 
			}
			catch(Exception e) 
			{
				e.printStackTrace(System.err);
				System.exit(1);
			}
		}
    }

	public void fixCollisionX(int tx)
	{
		
		
	}

	public void fixCollisionY(int ty)
	{
		
	}

	public void fixCollision(int tx, int ty)
	{
		if(prevX > x)
		{
			this.x = tx+w + 1;
		}
		else if(prevX < x)
		{
			this.x = tx-w - 1;
		}
		if(prevY > y)
		{
			this.y = ty +h + 1;
		}
		else if(prevY < y)
		{
			this.y = ty - h - 1;
		}
		
		System.out.println("fixed");
	}
    public void draw(Graphics g, int viewX, int viewY)
    {
        g.drawImage(linkImages[currentLinkImage],this.x-viewX,this.y-viewY,w,h,null);
    }

    public void setPrevious()
    {
        this.prevX = this.x;
        this.prevY = this.y;
    }
    public void update()
    {
        //implement
        
        return;
    }



	public void cycleDown()
	{ // index 5 - 12
		if(currentLinkImage < 5 || currentLinkImage >= 12)
		{
			currentLinkImage = 5;
		}
		currentLinkImage++;
		direction = 0;

	}
	
	public void cycleLeft()
	{ // index 13 - 22
		if(currentLinkImage < 13 || currentLinkImage >= 22)
		{
			currentLinkImage = 13;
		}
		currentLinkImage++;
		direction = 1;
	}

	public void cycleRight()
	{ // index 29 - 37
		if(currentLinkImage < 29 || currentLinkImage >= 37)
		{
			currentLinkImage = 29;
		}
		currentLinkImage++;
		direction = 3;
	}

	public void cycleUp()
	{ // index 39 - 49
		if(currentLinkImage < 39 || currentLinkImage >= 49)
		{
			currentLinkImage = 39;
		}
		currentLinkImage++;		
		direction = 2;
	}


	@Override
	public String toString()
	{
		return ("LINK@ " + x + "," + y + " " + prevX + "," + prevY);
	}


	public boolean inUp()
	{
		return (x+w/2>700);
	}
	public boolean inLeft()
	{
		return (x+w/2<700);
	}
	public boolean inDown()
	{
		return (y+h/2>500);
	}
	public boolean inRight()
	{
		
		return (y+h/2<500);
	}

	



}
