from typing import Optional

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import datetime
import pandas as pd
from pandas.core.indexes.datetimes import DatetimeIndex

def draw_aim(start_date: datetime.date, total_pages: int, pages_per_day_goal: int, save_path: Optional[str]=None) -> Optional[tuple[DatetimeIndex, list[int]]]:
    days_to_goal: int = total_pages / pages_per_day_goal
    goal_date: datetime.date = start_date + datetime.timedelta(days=days_to_goal)
    dates: DatetimeIndex = pd.date_range(start=start_date, end=goal_date, freq='D')
    pages: list[int] = [pages_per_day_goal * (len(dates)-1 -i) for i in range(len(dates))]
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
    draw_aim(datetime.date.today(), 590, 10, save_file)

    dates: DatetimeIndex
    pages: list[int]
    dates, pages = draw_aim(datetime.date.today(), 590, 10)
    print(type(dates), type(pages))
    print(dates.shape, len(pages))
