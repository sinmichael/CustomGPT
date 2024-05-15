import { Injectable } from '@nestjs/common';
import { RedisService } from './redis/redis.service';

@Injectable()
export class AppService {
  constructor(private readonly redisService: RedisService) {}

  async query(query: string) {
    const response = await this.redisService.publishAndWait(query);
    return response;
  }
}
