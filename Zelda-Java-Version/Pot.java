//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Implements Pot Class


import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.awt.Graphics;


public class Pot extends Sprite
{

    

    BufferedImage normPot = null;
    BufferedImage brokePot = null;
    int direction;
    boolean isBroke = false;
    int framesLeft = 20;
    int speed = 10;
    boolean sent = false;


    public Pot(int x, int y)
    {
        this.x = x;
        this.y = y;
        w = 30;
        h = 30;
        setTag("POT");
        if(normPot == null)
        {
            try //Imports png images
            {
                normPot = ImageIO.read(new File("ImageFolder/pot.png"));
                brokePot = ImageIO.read(new File("ImageFolder/pot_broken.png"));
            }
            catch(Exception e) 
            {
                e.printStackTrace(System.err);
                System.exit(1);
            }
        }
    }

    public Pot(Json ob) 
    {
        x = (int)ob.getLong("potX");
        y = (int)ob.getLong("potY");
        w = 30;
        h = 30;
            try //Imports png images
            {
                normPot = ImageIO.read(new File("ImageFolder/pot.png"));
                brokePot = ImageIO.read(new File("ImageFolder/pot_broken.png"));
            }
            catch(Exception e) 
            {
                e.printStackTrace(System.err);
                System.exit(1);
            }
        
        setTag("POT");
    }

    public void draw(Graphics g, int viewX, int viewY)
    {
        if(normPot == null)
        {
            try //Imports png images
            {
                normPot = ImageIO.read(new File("ImageFolder/pot.png"));
                brokePot = ImageIO.read(new File("ImageFolder/pot_broken.png"));
            }
            catch(Exception e) 
            {
                e.printStackTrace(System.err);
                System.exit(1);
            }
        }
        
        
        if(isBroke)
        {
            g.drawImage(brokePot, x-viewX+10, y-viewY+10,w,h, null);
            return;
        }
            g.drawImage(normPot, x-viewX+10, y-viewY+10,w,h, null);
            return;
    }
    public void sendPot(int direction)
    {
        sent = true;
        this.direction = direction;
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
    }

    public void update()
    {
      if(isBroke)
      {
        framesLeft--;
        speed = 0;
      }

      if(sent)
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
      }
    }

    public Json marshal()
    {
        Json ob = Json.newObject();
        ob.add("potX", this.x);
        ob.add("potY", this.y);
        return ob;
    }



    
}