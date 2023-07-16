from typing import Optional

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import datetime
import pandas as pd
from pandas.core.indexes.datetimes import DatetimeIndex

def draw_aim(start_date: datetime.date, total_pages: int, pages_per_day_goal: int, buffer_days: int = 0, save_path: Optional[str] = None) -> Optional[tuple[DatetimeIndex, list[int]]]:
    days_to_goal_without_buffer: int = int((total_pages + (pages_per_day_goal - 1)) / pages_per_day_goal)
    days_to_goal: int
    if buffer_days != 0:
        days_to_goal = days_to_goal_without_buffer + int(days_to_goal_without_buffer / buffer_days)
    else:
        days_to_goal = days_to_goal_without_buffer
    
    goal_date: datetime.date = start_date + datetime.timedelta(days=days_to_goal)
    
    dates: DatetimeIndex = pd.date_range(start=start_date, end=goal_date, freq='D')
    
    pages_per_day_buffered: int = total_pages / days_to_goal 
    
    pages: list[int] = [total_pages - i * pages_per_day_goal for i in range(days_to_goal_without_buffer+1)]

    if buffer_days > 0:
        num_buffers: int = days_to_goal - days_to_goal_without_buffer
        for i in range(num_buffers):
            print((i+1)*buffer_days+i, len(pages))
            pages.insert((i+1)*buffer_days+i, pages[(i+1)*buffer_days+i-1]) 

    if save_path is not None:
        fig: Figure
        ax: Axes
        fig, ax = plt.subplots()
        ax.plot(dates, pages, 'r-', label='Aim')
        ax.set_xlabel('date')
        ax.set_ylabel('pages')
        ax.set_title('Reading Aim, Goal Date: ' + goal_date.strftime("%m/%d/%Y"))
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.show()
        return
    else:
        return (dates, pages)
    

if __name__ == "__main__":
    save_file: str = "../../../tmp_files/aim.draw_aim.png"
    draw_aim(datetime.date.today(), 590, 10, save_path = save_file)
    save_file_not_splitted: str = "../../../tmp_files/aim.draw_aim.not_splitted.png"
    draw_aim(datetime.date.today(), 20, 11, save_path= save_file_not_splitted)

    save_file_buffer7: str = "../../../tmp_files/aim.draw_aim.buffer.png"
    draw_aim(datetime.date.today(), 590, 10, buffer_days= 7, save_path = save_file_buffer7)
    save_file_buffer7: str = "../../../tmp_files/aim.draw_aim.buffer.not_splitted.png"
    draw_aim(datetime.date.today(), 78, 11, buffer_days= 5, save_path = save_file_buffer7)

    
    dates: DatetimeIndex
    pages: list[int]
    dates, pages = draw_aim(datetime.date.today(), 590, 10, buffer_days= 7)
    print(type(dates), type(pages))
    print(dates.shape, len(pages))
