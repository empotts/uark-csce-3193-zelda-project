//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Implements Boomerang Class


import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.awt.Graphics;


public class Boomerang extends Sprite
{

    static BufferedImage boomImages[] = null;
    int speed = 10;
    int boomImageNum = 0;
    int direction;
    boolean isActive = true;

    public Boomerang(int x, int y, int direction)
    {
        this.x = x;
        this.y = y;
        w = 20;
        h = 20;
        this.direction = direction;
        
        
        if(boomImages == null)
		{
			try //Imports png images
			{
				boomImages = new BufferedImage[4];

				for(int i = 0; i < 4; i++)
				{
					String pathName = "ImageFolder/boomerang";
					if(i<9)
					{
						pathName = pathName + Integer.toString(i+1) + ".png";
						//System.out.println(pathName);
					}
					boomImages[i] = ImageIO.read(new File(pathName));
				}
				//System.out.println(x + "," + y); 
			}
			catch(Exception e) 
			{
				e.printStackTrace(System.err);
				System.exit(1);
			}
		}

        setTag("BOOMER");

    }

    public void draw(Graphics g, int viewX, int viewY)
    {
        g.drawImage(boomImages[boomImageNum],this.x-viewX,this.y-viewY,w,h,null);
    }

    public void update()
    {
        if(direction == 0)
        {
            y += speed;
        }
        if(direction == 1)
        {
            x -= speed;
        }
        if(direction == 2)
        {
            y -= speed;
        }
        if(direction == 3)
        {
            x += speed;
        }
        cycleImage();
    }

    public void cycleImage()
    {
        boomImageNum++;
        if(boomImageNum >=4)
        {
            boomImageNum = 0;
        }
    }



    
}
