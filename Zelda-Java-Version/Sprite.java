//Ethan Potts
//CSCE 3193 Assignment 5
//03-31-2023
//Implements Abstract Sprite class

import java.awt.Graphics;


public abstract class Sprite 
{
    int x;
    int y;
    int w;
    int h;
    String tag;

    public Sprite(int x, int y)
    {
        this.x = x;
        this.y = y;
        this.tag = "";

    }

    public void setTag(String s)
    {
        tag = s;
    }

    public String getTag()
    {
        return tag;
    }

    public Sprite()
    {
        x = y = w = h = 0;
    }

    abstract public void draw(Graphics g,int viewX, int viewY);

    //abstract public Json marshal();

    abstract public void update();

    @Override
    public String toString()
    {
        return "";
    }

    public boolean whatAmI(String s)
	{
		return tag==s; //MAY NEED TO CHANGE
	}

    public boolean collisionDetector1(Sprite sp) //FIX
	{
		if(y-5 + h < sp.y)
		{
			return false;
		}
		if(y+5 > sp.y + sp.h)
		{
			return false;
		}
		if(x+w-5 < sp.x)
		{
			return false;
		}
		if(x+5 > sp.x + sp.w)
		{
			return false;
		}
		
		return true;
	}

    
}
